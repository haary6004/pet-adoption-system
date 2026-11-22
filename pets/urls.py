from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.pet_list, name='list'),
    path('request/<int:pet_id>/', views.request_adoption, name='request'),
]
