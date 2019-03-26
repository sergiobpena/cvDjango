from django.contrib import admin

# Register your models here.

from .models import Niveis , CompInfor , CompProg , FormOficial , Curso , Direccion , DatosPersoais , Sector , ExperienciaProfesional , OutroDato , Curriculum 

admin.site.register(Niveis)
#@admin.register(Niveis)
#class NiveisAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Niveis,NiveisAdmin)


admin.site.register(CompInfor)
admin.site.register(CompProg)
admin.site.register(FormOficial)
admin.site.register(Curso)
admin.site.register(Direccion)
admin.site.register(DatosPersoais)
admin.site.register(Sector)
admin.site.register(ExperienciaProfesional)
admin.site.register(OutroDato)
admin.site.register(Curriculum)