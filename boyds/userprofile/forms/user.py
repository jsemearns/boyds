from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		password = forms.CharField(widget=forms.PasswordInput)
		fields = ['username', 'password']