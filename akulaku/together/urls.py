from django.urls import path
from . import views

urlpatterns = [
    path('together', views.together, name='together'),
    path('base', views.base, name='base'),
    path('ina', views.ina, name='ina'),
    path('index', views.index, name='index'),
]