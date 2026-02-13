from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [

    path('', views.serviceList, name='serviceList'),

    path('add/', views.addService, name='addService'),

    path('delete/<int:id>/', views.deleteService, name='deleteService'),

    path('update/<int:id>/', views.updateService, name='updateService'),
]
