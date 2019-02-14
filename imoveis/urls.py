from django.urls import path
from. import views

urlpatterns = [
    path('', views.home),
    path('cliente/', views.cliente_list),
    path('cliente/<int:cliente_id>/', views.cliente_show),
    path('imovel/', views.imovel_list),
    path('imovel/<int:imovel_id>/', views.imovel_show),
    path('cliente/form/', views.cliente_form),
    path('cliente/<int:cliente_id>/edit/', views.cliente_edit),
    path('imovel/form/', views.imovel_form)
]