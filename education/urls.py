from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_list, name='education_list'),
    path('add/', views.add_education, name='add_education'),
    path('<int:pk>/edit/', views.edit_education, name='edit_education'),
    path('<int:pk>/delete/', views.delete_education, name='delete_education'),
]
