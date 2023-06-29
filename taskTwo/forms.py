from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import adminAddApp, userAppTask

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class CreateAdminUserForm(UserCreationForm):
    class Meta:
        model=User
        # fields='__all__'
        fields=['username','first_name','last_name','email','password1','password2','is_superuser','is_staff','is_active']


class uploadAdmin(forms.ModelForm):
    class Meta:
        model =adminAddApp
        fields=['userId','appName','appLink','appCategory','appSubCategory','adminAppPoints','adminAppImage']

class uploadUserSS(forms.ModelForm):
    class Meta:
        model =userAppTask
        fields=['adminappId','userappid','userAppName','userAppPoints','userAppImage']
