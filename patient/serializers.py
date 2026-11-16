from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'
         
         
class PatientRegistrationSerializer(serializers.ModelSerializer):
   confirm_password = serializers.CharField(required=True,)
   class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name','email', 'password' ,'confirm_password']
        
        def save(self):
            username = self.validated_data['username']
            email_ = self.validated_data['email']
            password = self.validated_data['password']
            password2 = self.validated_data['confirmed_password']
            
            if password != password2:
                raise serializers.ValidationError({
                    'error' : "Password Dosn't Matched ! "
                })
            if User.objects.filter(email!=email_):
                raise serializers.ValidationError({
                    'error' : "This Email Already Exists"
                })
                
            new_account = User(username = username , email = email_)
            print(new_account)
            new_account.set_password(password)
            new_account.save()
            return new_account