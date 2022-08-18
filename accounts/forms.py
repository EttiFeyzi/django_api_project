from django import forms
from accounts.models import MyUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['mobile',]