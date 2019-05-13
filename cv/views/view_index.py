from cv.models import *
from django.shortcuts import render
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
