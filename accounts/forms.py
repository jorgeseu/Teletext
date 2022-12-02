from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserData

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#         # class Meta:
#         #     # model = UserData

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserData
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserData
        fields = ('email',)