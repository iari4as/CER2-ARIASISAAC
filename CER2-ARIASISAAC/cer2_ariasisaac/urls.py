"""
URL configuration for cer2_ariasisaac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from core.views import eliminar_grupo_producto, envio_pedido, home,catalogo, solicitud,signup, protected, signout,signin,carrito, agregar_producto, eleminar_producto, restar_producto, limpiar_carrito
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('catalogo/',catalogo,name="catalogo"),
    path('solicitud/',solicitud, name="solicitud"),
    path('signup/', signup, name="signup"),
    path('protected/', protected, name="protected" ),
    path('logout/', signout, name="logout"),
    path('login/', signin, name="login"),
    path('carrito/', carrito, name="carrito"),
    path("pedidos/", envio_pedido, name="pedidos"),

    path('agregar/<int:producto_id>/', agregar_producto, name="add"),
    path('eliminar/<int:producto_id>/', eleminar_producto, name="del"),
    path('restar/<int:producto_id>/', restar_producto, name="res"),
    path('eliminar_grupo/<int:producto_id>/', eliminar_grupo_producto, name='eliminar_grupo'),
    path('limpiar/', limpiar_carrito, name= "cls"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
