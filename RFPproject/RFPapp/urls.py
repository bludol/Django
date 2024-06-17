from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kapely/', views.kapely_list, name='kapely_list'),
    path('osoby/', views.osoby_list, name='osoby_list'),
    path('pisnicky/', views.pisnicky_list, name='pisnicky_list'),
    path('kapela/<int:kapela_id>/', views.kapela_detail, name='kapela_detail'),
]