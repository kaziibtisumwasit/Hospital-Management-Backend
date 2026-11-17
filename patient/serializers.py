from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Patient
        fields = '__all__'


class PatientRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data.get('first_name', '')
        last_name = self.validated_data.get('last_name', '')
        email_ = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password != password2:
            raise serializers.ValidationError({
                'error': "Password Doesn't Match!"
            })
        if User.objects.filter(email=email_).exists():
            raise serializers.ValidationError({
                'error': "This Email Already Exists"
            })

        new_account = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email_,
        )
        new_account.set_password(password)
        new_account.is_active = False  # Set the user as inactive until email verification  
        new_account.save()
        return new_account