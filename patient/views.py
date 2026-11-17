from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer , PatientRegistrationSerializer , UserLoginSerializer
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode ## ek language thke onno language e convert kortesi
from django.utils.encoding import force_bytes # it's a function which is make more effecient encording
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework.authtoken.models import Token

##For Sending  Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string





class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all() ## For Get Req
    serializer_class = PatientSerializer
    

## ApiView can use any where like classbased View.
class PatientRegistrationView(APIView):
    serializer_class = PatientRegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user) ## defalut_token_genator is make current user token
            print('Token:', token  )
            ## Current User er jonno ekta unique URL generate korlam using urlsafe_base64_encode and force_bytes. This URL will be used to verify the user's email address.
            uid = urlsafe_base64_encode(force_bytes(user.pk)) ## urlsafe_base64_encode is used to encode the user id in base64 format. force_bytes is used to convert the user id to bytes format.
            print('UID:', uid)
            confirm_link =f"http://127.0.0.1:8000/patients/active/{uid}/{token}/" ## confirm_link is the URL that will be sent to the user's email address for verification.
            
            email_subject = 'Activate your account'
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '' , to=[user.email])
            email.attach_alternative(email_body , "text/html")
            email.send()
            
            return Response("Check Your Mail To Confirm Your Account Varification")
            
        
        return Response(serializer.errors)
    
    
    
    
def activate_account(request, uid64 , token):
    try:
        uid = urlsafe_base64_decode(uid64).decode() ## urlsafe_base64_decode is used to decode the user id from base64 format. decode is used to convert the bytes format to string format.
        user = User._default_manager.get(pk=uid) ## get the user object using the decoded user id.
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token): ## check_token is used to check if the token is valid for the given user.
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully. You can now log in.')
        return redirect('patient-login') 
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('patient-register')



class userLoginApiView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                # return Response({'message': 'Login successful'})
                token , _ = Token.objects.get_or_create(user=user) # if object exists then get it otherwise create it
                return Response({'token': token.key , 'user_id' : user.id})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        return Response(serializer.errors, status=400)     


## At Login time we give new token to user & save the tocken on te database,& When user logout then we delete the token from the database. So that user can't access the API without login again.We use tocken creation & deltetion process for security purpose. If we don't delete the token then user can access the API without login again. So we delete the token from the database when user logout.


class userLogoutView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()  # Delete the user's token to log them out
            logout(request)  # Log out the user from the session
            messages.success(request, 'You have been logged out successfully.')
            return redirect('patient-login')  # Redirect to the login page after logout
        else:
            return Response({'error': 'User is not authenticated'}, status=400)
