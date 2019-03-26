from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , PasswordResetForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, label='Correo electrónico',
                            widget=forms.EmailInput())
    username = forms.CharField(label='Usuario', min_length=4, max_length=150,required=True,
                               help_text='Introduce nome de usuario.Lonxitude mínima 4 caracteres e maximo 150 .Letras,'
                                         ' números e @/./+/-/_ solo.')
    password1 = forms.CharField(label='Contrasinal',
                                required=True,
                                help_text="- O contrasinal debe estar formado de alomenos 8 caracteres",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación do contrasinal',
                                required=True,
                                help_text='Repite o contrasinal indicado para a sua verificación',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginFormulario(AuthenticationForm):
    username = forms.CharField(label='Nome de usuario', required=True)
    password = forms.CharField(label='Contrasinal', required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')


class ReseteoContrasinalFormulario(PasswordResetForm):
    email = forms.EmailField(label='Correo electronico', required=True)

    class Meta:
        model = User
        fields = 'email'
