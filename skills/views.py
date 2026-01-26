from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill
from .forms import SkillForm


def skills_list(request):
    """Skills page"""
    skills_by_category = {
        'programming': Skill.objects.filter(category='programming'),
        'frameworks': Skill.objects.filter(category='frameworks'),
        'tools': Skill.objects.filter(category='tools'),
        'soft': Skill.objects.filter(category='soft'),
    }
    return render(request, 'skills/skills.html', {
        'skills_by_category': skills_by_category,
        'is_admin': request.user.is_authenticated
    })


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
    
    return render(request, 'skills/skill_form.html', {'form': form, 'action': 'Add'})


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
    
    return render(request, 'skills/skill_form.html', {'form': form, 'action': 'Edit'})


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
