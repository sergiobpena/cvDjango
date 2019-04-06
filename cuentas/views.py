

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import PasswordResetView , LoginView
from .forms import SignUpForm , LoginFormulario , ReseteoContrasinalFormulario

from django.urls import reverse_lazy

from django.views.generic import FormView, TemplateView, RedirectView

from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


class LoginVista (LoginView):
    form_class = LoginFormulario
    template_name ='login.html'
    success_url = reverse_lazy("index")


class ReseteaContrasinalVista(PasswordResetView):
    form_class = ReseteoContrasinalFormulario



