from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Experience
from .forms import ExperienceForm


def experience_list(request):
    """Experience page"""
    experiences = Experience.objects.all()
    return render(request, 'experience/experience.html', {
        'experience_list': experiences,
        'is_admin': request.user.is_authenticated
    })


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
    
    return render(request, 'experience/experience_form.html', {'form': form, 'action': 'Add'})


@login_required
def edit_experience(request, pk):
    """Edit experience"""
    exp = get_object_or_404(Experience, pk=pk)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience updated successfully')
            return redirect('admin_dashboard')
    else:
        form = ExperienceForm(instance=exp)
    
    return render(request, 'experience/experience_form.html', {'form': form, 'action': 'Edit'})


@login_required
def delete_experience(request, pk):
    """Delete experience"""
    exp = get_object_or_404(Experience, pk=pk)
    
    if request.method == 'POST':
        exp.delete()
        messages.success(request, 'Experience deleted successfully')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/confirm_delete.html', {
        'item': exp,
        'item_type': 'Experience'
    })
