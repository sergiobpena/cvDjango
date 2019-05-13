from cv.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

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