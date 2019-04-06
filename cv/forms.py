from django import forms
from .models import ExperienciaProfesional,FormOficial,DatosPersoais,Direccion,Curso,CompProg,CompInfor
from django.core.exceptions import ValidationError


class ExperienciaProfsForm(forms.ModelForm):

    # validacion de data de finalizacion
    def clean_dataFin(self):
        fin = self.cleaned_data['dataFin']
        comezo = self.cleaned_data['dataInicio']
        if fin:
            pass
        else:
            if fin < comezo:
                raise ValidationError(_('Data de finalización inválida.'))
            else:
                pass
        return fin

    class Meta:
        model = ExperienciaProfesional
        exclude = ['usuario']


class FormacionOficialForm(forms.ModelForm):

    def clean_dataFin(self):
        fin = self.cleaned_data['dataFin']
        comezo = self.cleaned_data['dataInicio']
        if fin:
            if fin < comezo:
                raise ValidationError(_('Data de finalización inválida.'))
            else:
                pass

        return fin

    class Meta:
        model = FormOficial
        exclude = ['usuario']


class DatosPersoaisForm(forms.ModelForm):
    class Meta:
        model = DatosPersoais
        exclude = ['usuario']


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = ['usuario']


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        exclude = ['usuario']


class CompInforForm(forms.ModelForm):
    class Meta:
        model = CompInfor
        exclude = ['usuario']


class CompProgForm(forms.ModelForm):
    class Meta:
        model = CompProg
        exclude = ['usuario']
