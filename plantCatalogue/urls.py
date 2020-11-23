"""plantCatalogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView
from plants import views as plants_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', plants_view.query, name='search'),
    path('', plants_view.plantList),
    path('genus', plants_view.genusList),
    path('family', plants_view.familyList),
    path('order', plants_view.orderList),
    path('class', plants_view.classList),
    path('plants/<str:slug>', plants_view.plant, name='plant'),
    path('genus/<str:slug>', plants_view.genus, name='genus'),
    path('family/<str:slug>', plants_view.family, name='family'),
    path('order/<str:slug>', plants_view.order, name='order'),
    path('class/<str:slug>', plants_view.divisionClass, name='class'),
    path('serviceworker.js', (TemplateView.as_view(
        template_name="serviceworker.js",
        content_type='application/javascript',
        )), name='serviceworker.js'),
]
