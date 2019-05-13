from cv.forms import ExperienciaProfsForm,FormacionOficialForm,CursoForm,DatosPersoaisForm,DireccionForm,CompInforForm,CompProgForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render , redirect
from .view_perfil import estableceContexto
from django.contrib.auth.models import User


def crearExperiencia(request):
    user = User.objects.first()
    diccionario_contexto = estableceContexto(user)
    if request.method == 'POST':
        form = ExperienciaProfsForm(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.usuario = user
            experiencia.save()
            # diccionario_contexto['form']=form
            return redirect('experiencia')
    else:
        form = ExperienciaProfsForm
    diccionario_contexto['form'] = form
    return render(request, 'editar_perfil.html', context=diccionario_contexto)


class CrearExperienciaView(LoginRequiredMixin,View):
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    form = ExperienciaProfsForm
    template_name = 'editar_perfil.html'

    def get(self, request):
        diccionario_contexto = estableceContexto(self.request.user)
        diccionario_contexto['form'] = self.form
        return render(request, 'editar_perfil.html', diccionario_contexto)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.usuario = self.request.user
            experiencia.save()
        else:
            form = self.form
        return redirect('perfil')


class CrearFormacionOficialView(CrearExperienciaView):
    form = FormacionOficialForm


class CrearCursoView(CrearExperienciaView):
    form = CursoForm

class CreaDatosPersoaisView(CrearExperienciaView):
    form = DatosPersoaisForm

class CreaDireccionView(CrearExperienciaView):
    form=DireccionForm

class CreaCompInfor(CrearExperienciaView):
    form = CompInforForm

class CreaCompProgView(CrearExperienciaView):
    form = CompProgForm
