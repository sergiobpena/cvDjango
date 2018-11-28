# Generated by Django 2.1.2 on 2018-11-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20181128_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compinfor',
            options={'verbose_name': 'Competencias informáticas'},
        ),
        migrations.AlterModelOptions(
            name='compprog',
            options={'verbose_name': 'Linguaxes de programación'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['dataFin', 'dataInicio'], 'verbose_name': 'Formación non oficial'},
        ),
        migrations.AlterModelOptions(
            name='datospersoais',
            options={'verbose_name': 'Datos persoais'},
        ),
        migrations.AlterModelOptions(
            name='experienciaprofesional',
            options={'ordering': ['dataFin', 'dataInicio'], 'verbose_name': 'Experiencia Profesional'},
        ),
        migrations.AlterModelOptions(
            name='formoficial',
            options={'ordering': ['dataFin', 'dataInicio'], 'verbose_name': 'Formación oficial'},
        ),
        migrations.AlterModelOptions(
            name='niveis',
            options={'verbose_name': 'Niveis'},
        ),
        migrations.AlterModelOptions(
            name='outrodato',
            options={'verbose_name': 'Outros datos de interese'},
        ),
        migrations.AddField(
            model_name='curso',
            name='escola',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Centro de estudo'),
        ),
        migrations.AddField(
            model_name='curso',
            name='nomeCurso',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome do curso'),
        ),
        migrations.AddField(
            model_name='datospersoais',
            name='telefono',
            field=models.IntegerField(blank=True, null=True, verbose_name='Numero de telefono'),
        ),
        migrations.AlterField(
            model_name='compinfor',
            name='software',
            field=models.CharField(max_length=50, verbose_name='Software'),
        ),
        migrations.AlterField(
            model_name='compinfor',
            name='tipoCompe',
            field=models.CharField(max_length=50, verbose_name='Competencia'),
        ),
        migrations.AlterField(
            model_name='compprog',
            name='outra_info',
            field=models.TextField(blank=True, verbose_name='Informacion adicional'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='compAdq',
            field=models.TextField(verbose_name='Competencias adquiridas'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='dataFin',
            field=models.DateField(blank=True, help_text='En blanco se estás estudando na actualidade', null=True, verbose_name='Data finalización'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='dataInicio',
            field=models.DateField(verbose_name='Data inicio'),
        ),
        migrations.AlterField(
            model_name='datospersoais',
            name='apel1',
            field=models.CharField(max_length=50, verbose_name='1º Apelido'),
        ),
        migrations.AlterField(
            model_name='datospersoais',
            name='apel2',
            field=models.CharField(max_length=50, verbose_name='2º Apelido'),
        ),
        migrations.AlterField(
            model_name='datospersoais',
            name='correoe',
            field=models.EmailField(max_length=254, verbose_name='Correo eléctronico'),
        ),
        migrations.AlterField(
            model_name='datospersoais',
            name='dataNac',
            field=models.DateField(verbose_name='Data de nacemento'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='andar',
            field=models.IntegerField(verbose_name='Piso'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='letraPis',
            field=models.CharField(max_length=1, verbose_name='Letra Piso'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numPis',
            field=models.IntegerField(verbose_name='Portal'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='rua',
            field=models.CharField(max_length=80, verbose_name='Rúa'),
        ),
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='dataFin',
            field=models.DateField(blank=True, help_text='En blanco se continúas na actualidade', null=True, verbose_name='Data Finalización'),
        ),
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='dataInicio',
            field=models.DateField(verbose_name='Data inicio'),
        ),
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='empresa',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='posto',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='formoficial',
            name='dataFin',
            field=models.DateField(blank=True, help_text='En blanco se estás estudando na actualidade', null=True, verbose_name='Data finalización'),
        ),
        migrations.AlterField(
            model_name='formoficial',
            name='dataInicio',
            field=models.DateField(verbose_name='Data de inicio'),
        ),
        migrations.AlterField(
            model_name='formoficial',
            name='escola',
            field=models.CharField(max_length=80, verbose_name='Centro de estudo'),
        ),
        migrations.AlterField(
            model_name='niveis',
            name='nivel',
            field=models.CharField(max_length=50, verbose_name='Nivel'),
        ),
        migrations.AlterField(
            model_name='outrodato',
            name='texto1',
            field=models.CharField(max_length=50, verbose_name='Dato de interés'),
        ),
        migrations.AlterField(
            model_name='outrodato',
            name='texto2',
            field=models.TextField(verbose_name='Información adicional'),
        ),
    ]
