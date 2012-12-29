from django.contrib.auth.backends import ModelBackend
from django.core.validators import email_re
from django.contrib.auth.models import User


class AuthenticationBackend(ModelBackend):

    def authenticate(self, username=None, password=None):
        if email_re.search(username):
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return super(
                        AuthenticationBackend,
                        self).authenticate(
                            user.username,
                            password)
            except User.DoesNotExist:
                return None
        return super(
            AuthenticationBackend,
            self).authenticate(username, password)
