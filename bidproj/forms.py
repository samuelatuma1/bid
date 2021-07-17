from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Registration(forms.ModelForm):
    
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    def validate_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        
        if password1 != password2:
            raise forms.ValidationError('passwords do not match')
        elif len(password1) < 6:
            raise forms.ValidationError('Password must be at least six characters long')
        
        
        return self.cleaned_data['password1']