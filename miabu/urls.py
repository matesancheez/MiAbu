"""
URL configuration for miabu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from miabu import settings
from usuario.views import *

from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf.urls import handler404
 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path("agregar/", agregar_gasto.as_view(), name="agregar"),
    path("editar/<pk>/", editar_gasto.as_view(), name="editar"),
    path("eliminar/<pk>/", eliminar_gasto, name="eliminar"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home/", view_home ,name="home"),
    path("home/<str:mes>/", view_home2 ,name="home2"),
    path("detalle/<pk>", view_detalle.as_view(), name="detalle")
]

handler404 = mi_error_404.as_view()

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]

urlpatterns += [
    re_path(r'^staticfiles/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    })
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
