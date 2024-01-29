from typing import Any
from django import forms
from users.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(required=True,
                               min_length = 4,
                               max_length = 50, 
                               widget = forms.TextInput(
                                   attrs={'class':'form-control',
                                          'id':'username',
                                          'placeholder':'Username'}))
    
    email = forms.EmailField(required=True,widget = forms.EmailInput(
                                   attrs={'class':'form-control',
                                          'id':'email',
                                          'placeholder':'example@gmail.com'}))
    
    password = forms.CharField(required=True,widget = forms.PasswordInput(
                                   attrs={'class':'form-control',
                                          'id':'password'}))
    
    password2 = forms.CharField(label='Confirmar Password',required=True,widget = forms.PasswordInput(
                                   attrs={'class':'form-control',
                                          'id':'password2'}))
    

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
              raise forms.ValidationError('El username ya está en uso, porfavor ingresa otro')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
              raise forms.ValidationError('El email ya está en uso, porfavor ingresa otro')
        return email
    
    def clean(self):
         cleaned_data = super().clean()

         if cleaned_data.get('password2') != cleaned_data.get('password'):
              self.add_error('password2', 'Las passwords no coinciden')
         
    def save(self):
        return User.objects.create_user(
              self.cleaned_data.get('username'),
              self.cleaned_data.get('email'),
              self.cleaned_data.get('password'),
         )