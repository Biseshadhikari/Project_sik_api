from rest_framework import generics, status
from rest_framework.response import Response
from core.models import *
from core.serializer import PasswordResetOTPSerializer
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class SendPasswordResetEmailView(generics.CreateAPIView):
    serializer_class = PasswordResetOTPSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'User with this email does not exist.',"success":False})
        
        # Generate a random OTP
        otp = ''.join(random.choice('0123456789') for _ in range(6))
        
        # Store the OTP and user in the PasswordResetOTP model
        PasswordResetOTP.objects.create(user=user, otp=otp)
        
        # Send the OTP via email
        subject = 'Password Reset OTP'
        message = f'Your OTP for password reset is: {otp}'
        email_from = settings.EMAIL_HOST_USER  # Set your sender email
        recipient_list = [email]
        
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        
        return Response({'message': 'Email sent with OTP.',"success":True})
    
class VerifyPasswordResetOTPView(generics.UpdateAPIView):
    serializer_class = PasswordResetOTPSerializer

    def update(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')
        newpassword = request.data.get('newpassword')
        print(otp)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'User with this email does not exist.',"success":False})
        
        try:
            reset_otp = PasswordResetOTP.objects.get(user=user, otp=otp)
        except PasswordResetOTP.DoesNotExist:
            return Response({'message': 'Invalid OTP.',"success":False})
        
        # Check if OTP is still valid (e.g., within a certain time frame)
        expiration_time = reset_otp.created_at + timedelta(minutes=15)  # OTP expires in 15 minutes
        
        if timezone.now() > expiration_time:
            return Response({'message': 'OTP has expired.',"success":False})
        
        # Reset the user's password (You can replace this logic with your own password reset code)
        new_password = newpassword  # Generate a new password
        user.set_password(new_password)
        user.save()
        
        # Delete the used OTP
        reset_otp.delete()
        
        return Response({'message': 'Password reset successfully.',"success":True})

