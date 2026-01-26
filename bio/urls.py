from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/bio/edit/', views.edit_bio, name='edit_bio'),
]
