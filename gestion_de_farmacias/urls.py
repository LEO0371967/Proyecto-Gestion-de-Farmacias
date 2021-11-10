"""gestion_de_farmacias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login

#from gestion_de_farmacias.views import login, inicio
from gestion_de_farmacias import views
from gestionUsuarios.views import RegistrarUsuario, EditarUsuario, ListaDeUsuarios, ListarRecetas, EditarReceta, UsuarioReceta
from gestionStock.views import ListarMedicamentos, Stock, EditarStock

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),

    #path('login/', views.login, name="login"),
    #path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    #path('logout/', logout_then_login.as_view(template_name='login.html'), name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),



    #path('medicamentos/', views.medicamentos, name="medicamentos"),
    path('medicamentos/', ListarMedicamentos.as_view(), name="medicamentos"),
    #path('buscar_medicamento/', buscar_medicamento, name="buscar_medicamento"),


    path('stock/', Stock.as_view(), name="stock"),
    #path('crear_stock/', views.LoteCreate.as_view(), name="cerar_stock"),
    path('editar_stock/<int:pk>', EditarStock.as_view(), name="editar_stock"),


    #path('receta/<int:receta_numero>/<str:usuario>', views.receta, name="receta"),
    #path('recetas/', views.recetas, name="recetas"),
    path('recetas/', ListarRecetas.as_view(), name="recetas"),
    path('editar_receta/<int:pk>', EditarReceta.as_view(), name="editar_stock"),
    path('mis_recetas/', UsuarioReceta.as_view(), name="mis_recetas"),

    path('lista_de_usuarios/', ListaDeUsuarios.as_view(), name="lista_de_usuarios"),
    path('registrar_usuario/', RegistrarUsuario.as_view(), name="registrar_usuario"),
    path('editar_usuario/<int:pk>', EditarUsuario.as_view(), name="editar_usuario"),
    
    
    path('carga_medicamentos/', views.carga_medicamentos, name="carga_medicamentos"),
    path('carga_usuarios/', views.carga_usuarios, name="carga_usuarios"),

    
]