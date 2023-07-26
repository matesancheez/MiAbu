from miabu import settings
from usuario.views import *

from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf.urls import handler404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path("agregar/", login_required(agregar_gasto.as_view()), name="agregar"),
    path("editar/<pk>/", login_required(editar_gasto.as_view()), name="editar"),
    path("eliminar/<pk>/", eliminar_gasto, name="eliminar"),
    path("logout/", login_required(LogoutView.as_view()), name="logout"),
    path("home/", view_home ,name="home"),
    path("home/<str:mes>/", view_home2 ,name="home2"),
    path("detalle/<pk>", login_required(view_detalle.as_view()), name="detalle")
]


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
