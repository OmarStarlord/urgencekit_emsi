from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Attempting to authenticate user with email: {username}")  # Print the email
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None