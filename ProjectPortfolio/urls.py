"""
URL configuration for ProjectPortfolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Import models for dashboard
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project


def admin_login(request):
    """Admin login page"""
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'admin/login.html')


def admin_logout_view(request):
    """Logout and redirect to home"""
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


@login_required
def admin_dashboard(request):
    """Admin dashboard with overview"""
    context = {
        'bio': Bio.objects.first(),
        'education_list': Education.objects.all(),
        'education_count': Education.objects.count(),
        'skills_list': Skill.objects.all(),
        'skills_count': Skill.objects.count(),
        'experience_list': Experience.objects.all(),
        'experience_count': Experience.objects.count(),
        'projects_list': Project.objects.all(),
        'projects_count': Project.objects.count(),
    }
    return render(request, 'admin/dashboard.html', context)


urlpatterns = [
    path('django-admin/', admin.site.urls),
    
    # Authentication
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout_view, name='admin_logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    
    # App URLs
    path('', include('bio.urls')),
    path('education/', include('education.urls')),
    path('skills/', include('skills.urls')),
    path('experience/', include('experience.urls')),
    path('projects/', include('projects.urls')),
]
