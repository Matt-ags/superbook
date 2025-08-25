from django import forms
from .models import Perfil
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['descricao', 'cc_myself']  # campos do perfil



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
