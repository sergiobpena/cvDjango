from cv.models import *
from cv.forms import *
from django.shortcuts import render,redirect , get_object_or_404
from .view_perfil import estableceContexto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

def editaExperiencia(request, pk):
    experiecia = get_object_or_404(ExperienciaProfesional, id=pk)

    if request.method == 'POST':
        form = ExperienciaProfsForm(request.POST, instance=experiecia)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.usuario = request.user
            exp.save()
            return redirect('perfil')
    else:
        form = ExperienciaProfsForm(instance=experiecia)

    diccionario_contexto = estableceContexto(request.user)
    diccionario_contexto['form'] = form
    return render(request, 'editar_perfil.html', diccionario_contexto)


class EditaCursoView(LoginRequiredMixin,View):
    modelo = Curso
    formulario = CursoForm
    plantilla = 'editar_perfil.html'
    instancia=None

    # def __init__(self,**kwargs):
    #     super().__init__()
    #     pk = kwargs.get('pk')
    #     self.instancia = get_object_or_404(self.modelo, id=pk)

    def renderiza(self, request):
        diccionario_contexto = estableceContexto(request.user)
        diccionario_contexto['form'] = self.formulario
        return render(request, self.plantilla, diccionario_contexto)

    def get(self, request,**kwargs):
        pk = kwargs.get('pk')
        instancia = get_object_or_404(self.modelo, id=pk)
        self.formulario = self.formulario(instance=instancia)
        return self.renderiza(request)

    def post(self, request,**kwargs):
        pk = kwargs.get('pk')
        instancia = get_object_or_404(self.modelo,id= pk)
        self.formulario = self.formulario(request.POST, instance=instancia)
        if self.formulario.is_valid():
            modelo = self.formulario.save(commit=False)
            modelo.usuario = request.user
            modelo.save()
            return redirect('perfil')
        return self.renderiza(request)


class EditaFormOficialView(EditaCursoView):
    modelo = FormOficial
    formulario = FormacionOficialForm


class EditaDatosPersoaisView(EditaCursoView):
    modelo = DatosPersoais
    formulario = DatosPersoaisForm


class EditaDireccionView(EditaCursoView):
    modelo = Direccion
    formulario = DireccionForm

class EditaCompProgView(EditaCursoView):
    modelo = CompProg
    formulario = CompProgForm

class EditaCompInformView(EditaCursoView):
    modelo = CompInfor
    formulario = CompInforForm

