from django import forms
from .models import ExperienciaProfesional

class ExperienciaProfsForm(forms.ModelForm):

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

