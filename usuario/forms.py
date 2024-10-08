from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(
      label= ("Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
  )