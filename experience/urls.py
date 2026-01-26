from django.urls import path
from . import views

urlpatterns = [
    path('', views.experience_list, name='experience_list'),
    path('add/', views.add_experience, name='add_experience'),
    path('<int:pk>/edit/', views.edit_experience, name='edit_experience'),
    path('<int:pk>/delete/', views.delete_experience, name='delete_experience'),
]
