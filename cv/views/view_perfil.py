

from django.views.generic import  View, ListView
from django.shortcuts import  redirect, render

from django.contrib.auth.mixins import LoginRequiredMixin

from cv.models import CompInfor, CompProg, FormOficial, Curso, Direccion, DatosPersoais, Sector, ExperienciaProfesional, \
    OutroDato, Curriculum

class ExperienciaProfesionalView(ListView):
    model = ExperienciaProfesional
    context_object_name = 'exp_profes'  # nome da lista para a variable de plantilla
    # queryset=ExperienciaProfesional.objects.filter(concello__icontains='santiago')[:1]
    template_name = 'cv/experiencia.html'
    # def get_queryset(self, **kwargs):
    # context = super(ExperienciaProfesionalView, self).get_context_data(**kwargs)
    # context['some_data'] = 'This is just some data'
    # return context


def estableceContexto(usuario):
    diccionario_contexto = {
        'curso': Curso.objects.filter(usuario=usuario),
        'formOficial': FormOficial.objects.filter(usuario=usuario),
        'experienciaProfesional': ExperienciaProfesional.objects.filter(usuario=usuario),
        'direccion':Direccion.objects.filter(usuario=usuario),
        'datos':DatosPersoais.objects.filter(usuario=usuario),
        'compInfor':CompInfor.objects.filter(usuario=usuario),
        'compProg':CompProg.objects.filter(usuario=usuario)
    }
    return diccionario_contexto


class PerfilView(LoginRequiredMixin,View):
    template_name = 'perfil.html'

    def get(self, request):
        usuario = self.request.user
        diccionario_contexto = estableceContexto(usuario)
        return render(request, 'perfil.html', context=diccionario_contexto)
