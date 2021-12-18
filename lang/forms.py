from django.contrib.auth.forms import AuthenticationForm

from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    user_cache = None

    def get_user(self):
        return self.user_cache