from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm


def projects_list(request):
    """Projects page"""
    project_list = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects_list': project_list,
        'is_admin': request.user.is_authenticated
    })


@login_required
def add_project(request):
    """Add new project"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully')
            return redirect('admin_dashboard')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form, 'action': 'Add'})


@login_required
def edit_project(request, pk):
    """Edit project"""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully')
            return redirect('admin_dashboard')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'projects/project_form.html', {'form': form, 'action': 'Edit'})


@login_required
def delete_project(request, pk):
    """Delete project"""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/confirm_delete.html', {
        'item': project,
        'item_type': 'Project'
    })
