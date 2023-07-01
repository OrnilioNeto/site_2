"""
URL configuration for cadastro_servicos project.

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
from django.contrib import admin
from django.urls import path
from div_site_2 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from usuarios import views as usuarios_views

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('conta/', usuarios_views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('', views.home, name='home'),
    path('cadastro/', views.cadastramento, name='cadastro'),
    path('tela/', views.visualizacao, name='tela'),
    path('cadastro/<int:id_produto>', views.editar, name='editar'),
    path('tela/<int:id_produto>', views.detalhe, name='detalhe'),
    path('filtro/', views.filtro, name='filtro'),
    path('delete/<int:id_produto>', views.excluir, name='excluir'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
