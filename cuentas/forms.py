from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, label='Direccion de correo electronico',
                            widget=forms.EmailInput())
    username = forms.CharField(label='Usuario', min_length=4, max_length=150,
                               help_text='Introduce nome de usuario.Lonxitude mínima 4 caracteres e maximo 150 .Letras,'
                                         ' números e @/./+/-/_ solo.')
    password1 = forms.CharField(label='Contrasinal',
                                help_text="- O contrasinal debe estar formado de alomenos 8 caracteres",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación do contrasinal',
                                help_text='Repite o contrasinal indicado para a sua verificación',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
