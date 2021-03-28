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
from django.contrib.auth import views as auth_views

from plants.views import plantViews
from plants.views import accountViews

urlpatterns = [
    ########################################################
    # Plants
    path('search/', plantViews.query, name='search'),
    # TODO create landing page
    # path('', TemplateView.as_view(template_name="landing.html")),
    path('', plantViews.plantList, name='home'),
    path('plants', plantViews.plantList),
    path('genus', plantViews.genusList),
    path('family', plantViews.familyList),
    path('order', plantViews.orderList),
    path('class', plantViews.classList),
    path('plants/<str:slug>', plantViews.plant, name='plant'),
    path('genus/<str:slug>', plantViews.genus, name='genus'),
    path('family/<str:slug>', plantViews.family, name='family'),
    path('order/<str:slug>', plantViews.order, name='order'),
    path('class/<str:slug>', plantViews.divisionClass, name='class'),
    ########################################################
    # Accounts
    path('admin/', admin.site.urls),
    path('accounts/login/',
         auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path("accounts/logout/", accountViews.logoutUser, name= "logout"),
    path('accounts/profile/', accountViews.profile, name="profile"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register/", accountViews.register, name="register"),
    ########################################################
    # Other
    path('serviceworker.js', (TemplateView.as_view(template_name="serviceworker.js",
        content_type='application/javascript',)), name='serviceworker.js'),
]
