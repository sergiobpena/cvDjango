from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import  View, DeleteView , ListView
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy

from .models import CompInfor, CompProg, FormOficial, Curso, Direccion, DatosPersoais, Sector, ExperienciaProfesional, \
    OutroDato, Curriculum


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_compInfor = CompInfor.objects.all().count()
    num_compProg = CompProg.objects.all().count()
    num_cursos = Curso.objects.all().count()
    num_experiencia = ExperienciaProfesional.objects.all().count()
    num_datout = OutroDato.objects.all().count()
    num_formOficial = FormOficial.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
            'num_compInfor': num_compInfor,
            'num_compProg': num_compProg,
            'num_experiencia': num_experiencia,
            'num_datout': num_datout,
            'num_formOficial': num_formOficial,
            'num_visits': num_visits
        },
    )


class ExperienciaProfesionalView(ListView):
    model = ExperienciaProfesional
    context_object_name = 'exp_profes'  # nome da lista para a variable de plantilla
    # queryset=ExperienciaProfesional.objects.filter(concello__icontains='santiago')[:1]
    template_name = 'cv/experiencia.html'
    # def get_queryset(self, **kwargs):
    # context = super(ExperienciaProfesionalView, self).get_context_data(**kwargs)
    # context['some_data'] = 'This is just some data'
    # return context


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


# def editaExperiencia(request,pk):
#     experiencia=get_object_or_404(ExperienciaProfesional,pk=pk)
#     if request.method=='POST':
#         form=ExperienciaProfsForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return HttpResponseRedirect(reverse('experiencia'))
#     else:
#         form=ExperienciaProfsForm
#     diccionario_contexto=estableceContexto() + {'form':form}
#     return render(request,'editar_perfil.html',context=diccionario_contexto)

# class EditaFormacionOficialView(generic.UpdateView):
#     model = FormOficial
#     # post.updated_by = self.request.user
#     formacion=get_object_or_404(FormOficial,pk=pk)

class PerfilView(LoginRequiredMixin,View):
    template_name = 'perfil.html'

    def get(self, request):
        usuario = self.request.user
        diccionario_contexto = estableceContexto(usuario)
        return render(request, 'perfil.html', context=diccionario_contexto)


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


class BorraExperienciaView(LoginRequiredMixin,DeleteView):
    model = ExperienciaProfesional
    success_url = reverse_lazy('perfil')
    template_name = 'borra_item.html'


class BorraFormOficialView(BorraExperienciaView):
    model = FormOficial


class BorraCursoView(BorraExperienciaView):
    model = Curso


class BorraDireccionView(BorraExperienciaView):
    model = Direccion


class BorraDatosPersoaisView(BorraExperienciaView):
    model = DatosPersoais


class BorraCompInformView(BorraExperienciaView):
    model = CompInfor


class BorraCompProgView(BorraExperienciaView):
    model = CompProg
