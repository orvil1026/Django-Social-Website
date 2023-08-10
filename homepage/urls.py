from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.i18n import JavaScriptCatalog


app_name = "homepage"

urlpatterns = [

    path('', views.home, name='home'),
    path('nav/', views.nav, name ='nav')

    ]