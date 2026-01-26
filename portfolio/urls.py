from django.urls import path
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    
    # Authentication
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    
    # Admin dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Profile CRUD
    path('admin/profile/edit/', views.edit_profile, name='edit_profile'),
    
    # Education CRUD
    path('admin/education/add/', views.add_education, name='add_education'),
    path('admin/education/<int:pk>/edit/', views.edit_education, name='edit_education'),
    path('admin/education/<int:pk>/delete/', views.delete_education, name='delete_education'),
    
    # Skills CRUD
    path('admin/skill/add/', views.add_skill, name='add_skill'),
    path('admin/skill/<int:pk>/edit/', views.edit_skill, name='edit_skill'),
    path('admin/skill/<int:pk>/delete/', views.delete_skill, name='delete_skill'),
    
    # Experience CRUD
    path('admin/experience/add/', views.add_experience, name='add_experience'),
    path('admin/experience/<int:pk>/edit/', views.edit_experience, name='edit_experience'),
    path('admin/experience/<int:pk>/delete/', views.delete_experience, name='delete_experience'),
]
