from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import CustomUser  # Import the custom user model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'birthdate', 'password1', 'password2')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')
