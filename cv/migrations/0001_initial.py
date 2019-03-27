# Generated by Django 2.1.2 on 2019-03-27 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCompe', models.CharField(max_length=50, verbose_name='Competencia')),
                ('software', models.CharField(max_length=50, verbose_name='Software')),
                ('nivel', models.CharField(blank=True, choices=[('p', 'Principiante'), ('m', 'Intermedio'), ('e', 'Experto')], default='p', max_length=1, verbose_name='Nivel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comp_inform', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Competencias informáticas',
            },
        ),
        migrations.CreateModel(
            name='CompProg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linguaxe', models.CharField(max_length=50)),
                ('nivel', models.CharField(blank=True, choices=[('p', 'Principiante'), ('m', 'Intermedio'), ('e', 'Experto')], max_length=1, verbose_name='Nivel')),
                ('outra_info', models.TextField(blank=True, verbose_name='Informacion adicional')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comp_programacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Linguaxes de programación',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCurso', models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome do curso')),
                ('escola', models.CharField(blank=True, max_length=80, null=True, verbose_name='Centro de estudo')),
                ('dataInicio', models.DateField(verbose_name='Data inicio')),
                ('dataFin', models.DateField(blank=True, help_text='En blanco se estás estudando na actualidade', null=True, verbose_name='Data finalización')),
                ('duracion', models.CharField(max_length=6)),
                ('compAdq', models.TextField(verbose_name='Competencias adquiridas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Formación non oficial',
                'ordering': ['dataFin', 'dataInicio'],
            },
        ),
        migrations.CreateModel(
            name='DatosPersoais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apel1', models.CharField(max_length=50, verbose_name='1º Apelido')),
                ('apel2', models.CharField(max_length=50, verbose_name='2º Apelido')),
                ('dataNac', models.DateField(verbose_name='Data de nacemento')),
                ('correoe', models.EmailField(max_length=254, verbose_name='Correo eléctronico')),
                ('telefono', models.IntegerField(blank=True, null=True, verbose_name='Numero de telefono')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datos_persoais', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Datos persoais',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=80, verbose_name='Rúa')),
                ('numPis', models.IntegerField(verbose_name='Portal')),
                ('andar', models.IntegerField(verbose_name='Piso')),
                ('letraPis', models.CharField(max_length=1, verbose_name='Letra Piso')),
                ('concello', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciaProfesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posto', models.CharField(max_length=80)),
                ('empresa', models.CharField(max_length=80)),
                ('provincia', models.CharField(max_length=50)),
                ('concello', models.CharField(max_length=50)),
                ('funcions', models.TextField()),
                ('dataInicio', models.DateField(verbose_name='Data inicio')),
                ('dataFin', models.DateField(blank=True, help_text='En blanco se continúas na actualidade', null=True, verbose_name='Data Finalización')),
            ],
            options={
                'verbose_name': 'Experiencia Profesional',
                'ordering': ['dataFin', 'dataInicio'],
            },
        ),
        migrations.CreateModel(
            name='FormOficial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulacion', models.CharField(max_length=80)),
                ('dataInicio', models.DateField(verbose_name='Data de inicio')),
                ('dataFin', models.DateField(blank=True, help_text='En blanco se estás estudando na actualidade', null=True, verbose_name='Data finalización')),
                ('escola', models.CharField(max_length=80, verbose_name='Centro de estudo')),
                ('informacionAdicional', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_oficial', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Formación oficial',
                'ordering': ['dataFin', 'dataInicio'],
            },
        ),
        migrations.CreateModel(
            name='OutroDato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.CharField(max_length=50, verbose_name='Dato de interés')),
                ('texto2', models.TextField(verbose_name='Información adicional')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outros_datos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Outros datos de interese',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='experienciaprofesional',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.Sector'),
        ),
        migrations.AddField(
            model_name='experienciaprofesional',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exp_profs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='OutroDato',
            field=models.ManyToManyField(blank=True, null=True, to='cv.OutroDato'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='compInfor',
            field=models.ManyToManyField(blank=True, null=True, to='cv.CompInfor'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='compProg',
            field=models.ManyToManyField(blank=True, null=True, to='cv.CompProg'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='cursos',
            field=models.ManyToManyField(blank=True, null=True, to='cv.Curso'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='datosPersoais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.DatosPersoais'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.Direccion'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='experienciaProfesional',
            field=models.ManyToManyField(blank=True, null=True, to='cv.ExperienciaProfesional'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='formOficial',
            field=models.ManyToManyField(blank=True, null=True, to='cv.FormOficial'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to=settings.AUTH_USER_MODEL),
        ),
    ]
