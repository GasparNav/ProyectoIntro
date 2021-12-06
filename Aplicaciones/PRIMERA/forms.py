from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import material, comentario

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class materialForm(forms.ModelForm):

    class Meta:
        model = material
        fields = '__all__'

        widgets = {
            "fecha_subida": forms.SelectDateWidget()    
        }

class ComentariosForm(forms.ModelForm):

    class Meta:
        model = comentario
        fields = ('autor', 'texto',)