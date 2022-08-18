from django.contrib.auth.backends import ModelBackend
from accounts.models import MyUser

class MobileBackend(ModelBackend):
    def authenticate(self, request, username=None, passwored=None, **kwargs):
        mobile = kwargs['mobile']
        try:
            user = MyUser.objects.get(mobile=mobile)
        except MyUser.DoesNotExist:
            pass