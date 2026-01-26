from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Education, Skill, Experience
from .forms import ProfileForm, EducationForm, SkillForm, ExperienceForm


# ============ PUBLIC VIEWS ============

def home(request):
    """Home page with profile/bio"""
    profile = Profile.objects.first()
    return render(request, 'index.html', {
        'profile': profile,
        'is_admin': request.user.is_authenticated
    })

def education(request):
    """Education page"""
    education_list = Education.objects.all()
    return render(request, 'education.html', {
        'education_list': education_list,
        'is_admin': request.user.is_authenticated
    })

def skills(request):
    """Skills page"""
    skills_by_category = {
        'programming': Skill.objects.filter(category='programming'),
        'frameworks': Skill.objects.filter(category='frameworks'),
        'tools': Skill.objects.filter(category='tools'),
        'soft': Skill.objects.filter(category='soft'),
    }
    return render(request, 'skills.html', {
        'skills_by_category': skills_by_category,
        'is_admin': request.user.is_authenticated
    })

def experience(request):
    """Experience page"""
    experience_list = Experience.objects.all()
    return render(request, 'experience.html', {
        'experience_list': experience_list,
        'is_admin': request.user.is_authenticated
    })


# ============ AUTHENTICATION VIEWS ============

def admin_login(request):
    """Admin login page - redirects if already logged in"""
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

@login_required
def admin_logout(request):
    """Logout and redirect to home"""
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


# ============ ADMIN DASHBOARD ============

@login_required
def admin_dashboard(request):
    """Admin dashboard with overview"""
    context = {
        'profile': Profile.objects.first(),
        'education_count': Education.objects.count(),
        'skills_count': Skill.objects.count(),
        'experience_count': Experience.objects.count(),
        'education_list': Education.objects.all(),
        'skills_list': Skill.objects.all(),
        'experience_list': Experience.objects.all(),
    }
    return render(request, 'admin/dashboard.html', context)


# ============ PROFILE CRUD ============

@login_required
def edit_profile(request):
    """Edit or create profile"""
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('admin_dashboard')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'admin/profile_form.html', {'form': form})


# ============ EDUCATION CRUD ============

@login_required
def add_education(request):
    """Add new education entry"""
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education added successfully')
            return redirect('admin_dashboard')
    else:
        form = EducationForm()
    
    return render(request, 'admin/education_form.html', {'form': form, 'action': 'Add'})

@login_required
def edit_education(request, pk):
    """Edit education entry"""
    education = get_object_or_404(Education, pk=pk)
    
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education updated successfully')
            return redirect('admin_dashboard')
    else:
        form = EducationForm(instance=education)
    
    return render(request, 'admin/education_form.html', {'form': form, 'action': 'Edit'})

@login_required
def delete_education(request, pk):
    """Delete education entry"""
    education = get_object_or_404(Education, pk=pk)
    
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education deleted successfully')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/confirm_delete.html', {
        'item': education,
        'item_type': 'Education'
    })


# ============ SKILLS CRUD ============

@login_required
def add_skill(request):
    """Add new skill"""
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added successfully')
            return redirect('admin_dashboard')
    else:
        form = SkillForm()
    
    return render(request, 'admin/skill_form.html', {'form': form, 'action': 'Add'})

@login_required
def edit_skill(request, pk):
    """Edit skill"""
    skill = get_object_or_404(Skill, pk=pk)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully')
            return redirect('admin_dashboard')
    else:
        form = SkillForm(instance=skill)
    
    return render(request, 'admin/skill_form.html', {'form': form, 'action': 'Edit'})

@login_required
def delete_skill(request, pk):
    """Delete skill"""
    skill = get_object_or_404(Skill, pk=pk)
    
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/confirm_delete.html', {
        'item': skill,
        'item_type': 'Skill'
    })


# ============ EXPERIENCE CRUD ============

@login_required
def add_experience(request):
    """Add new experience"""
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience added successfully')
            return redirect('admin_dashboard')
    else:
        form = ExperienceForm()
    
    return render(request, 'admin/experience_form.html', {'form': form, 'action': 'Add'})

@login_required
def edit_experience(request, pk):
    """Edit experience"""
    experience = get_object_or_404(Experience, pk=pk)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience updated successfully')
            return redirect('admin_dashboard')
    else:
        form = ExperienceForm(instance=experience)
    
    return render(request, 'admin/experience_form.html', {'form': form, 'action': 'Edit'})

@login_required
def delete_experience(request, pk):
    """Delete experience"""
    experience = get_object_or_404(Experience, pk=pk)
    
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Experience deleted successfully')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/confirm_delete.html', {
        'item': experience,
        'item_type': 'Experience'
    })
