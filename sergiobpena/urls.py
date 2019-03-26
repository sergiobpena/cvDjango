"""sergiobpena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from cuentas import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Redirixe peticions o modulo cv
from django.urls import include
# inclue url autentificacion
from django.conf.urls import url

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    path('cv/', include('cv.urls')),
]
# Redireccion da raiz do sitio a /cv
urlpatterns += [
    path('', RedirectView.as_view(url='/cv/', permanent=True)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# inclue urls de autentificacion
urlpatterns += [url(r'^signup/$', accounts_views.signup, name='signup')]

urlpatterns += [url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')]

urlpatterns += [url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login')]

# urls para reseteo de contrasinal

urlpatterns += [url(r'^reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                                      email_template_name='password_reset_email.html',
                                                                      subject_template_name='password_reset_subject.txt'),
                    name='password_reset'), ]

urlpatterns += [url(r'^reset/done/$',
                    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                    name='password_reset_done'), ]

urlpatterns += [url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
                    name='password_reset_confirm')]

urlpatterns += [url(r'^reset/complete/$',
                    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
                    name='password_reset_complete')]

urlpatterns += [
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change')]

urlpatterns += [url(r'^settings/password/done/$',
                    auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
                    name='password_change_done')]
