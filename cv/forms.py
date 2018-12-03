from django import forms
from django.forms import Modelform
from .models import ExperienciaProfesional

class ExperienciaProfsForm(Modelform):

    #validacion de data de finalizacion
    def clean_dataFin(self):
        fin=self.cleaned_data['dataFin']
        comezo=self.cleaned_data['dataInicio']
        if fin :
            pass
        else:
            if fin < comezo :
                raise ValidationError(_('Invalid date - renewal in past'))
            else:
                pass
        return fin

    class Meta:
        model = ExperienciaProfesional
        fields = '__all__'

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/cv/")
    else:
        form = UserCreationForm()
    return render(request, "biblioteca/registro.html", {
        'form': form,
    })