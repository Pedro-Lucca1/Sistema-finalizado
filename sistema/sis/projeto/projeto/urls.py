"""
URL configuration for projeto project.

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
from django.urls import path, include
from .views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    # path('', include('clientes.urls')),
    path('clientes/', include('clientes.urls')),
    path('produtos/', include('produtos.urls')),
    path('fornecedores/', include('fornecedores.urls')),
     path('compras/', include('compras.urls')),
      path('vendas/', include('vendas.urls')),
    # path('api-clientes/', include('clientes.urls')),
    # path('api-produtos/', include('produtos.urls')),
    # path('fornecedores-produtos/', include('fornecedores.urls')),
    path('admin/', admin.site.urls),
]
