###LANZAR SCRIPT SHELL

#exec(open('script.py').read())


###USUARIOS

##Creacion de usuario
# from django.contrib.auth.models import User
# user = User.objects.create_user('s.bpena', 'serxio.botana@gmail.com', '12346ABc')
# user.save()

##Autentificacion
# from django.contrib.auth import authenticate
# user = authenticate(username="s.bpena", password='12346ABc')
# user


###CREACION DE MODELOS

##Competencias informaticas
from cv.models import CompInfor
# compInfor1=CompInfor(tipoCompe='CAD',software='autocad',usuario=user)
# compInfor1.save()
CompInfor.objects.all()
CompInfor.objects.get(id=1).get_absolute_url()
# compInfor2=CompInfor(tipoCompe='Ofimatica',software='excel',nivel='experto',usuario=user)
# compInfor2.save()
# compInfor3=CompInfor(tipoCompe='Programacion',software='Eclipse',nivel='experto',usuario=user)
# compInfor3.save()

##Competencias de programacion
# from cv.models import CompProg
# compProg1=CompProg(linguaxe='Java',usuario=user,outra_info='son dios')
# compProg1.save()

##Estudios oficiais
# from cv.models import FormOficial
#
# formacion1=FormOficial(titulacion='Ingenieria',dataInicio='09/06/2018',)


### GRUPOS
# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from users.models import User
# new_group, created = Group.objects.get_or_create(name ='new_group')



