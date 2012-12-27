from django.contrib.auth.backends import ModelBackend
from django.core.validators import email_re
from django.contrib.auth.models import User
from atados.atados.forms import RegistrationForm
from atados.atados.models import Profile
from registration.backends.default import DefaultBackend


class RegistrationBackend(DefaultBackend):

    def register(self, request, **kwargs):
        new_user = super(RegistrationBackend, self).register(request, **kwargs)

        new_profile = Profile.objects.create(user=new_user)
        new_profile.save()

        return new_user

    def post_registration_redirect(self, request, user):
        return ('atados:sign_up_complete', (), {})

    def post_activation_redirect(self, request, user):
        return ('atados:sign_up_confirmation_complete', (), {})

    def get_form_class(self, request):
        return RegistrationForm


class AuthenticationBackend(ModelBackend):

    def authenticate(self, username=None, password=None):
        if email_re.search(username):
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return super(AuthenticationBackend, self).authenticate(
                            user.username,
                            password)
            except User.DoesNotExist:
                return None
        return super(AuthenticationBackend, self).authenticate(username, password)
