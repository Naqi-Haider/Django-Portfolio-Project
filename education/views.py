from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Education
from .forms import EducationForm


def education_list(request):
    """Education page"""
    education_entries = Education.objects.all()
    return render(request, 'education/education.html', {
        'education_list': education_entries,
        'is_admin': request.user.is_authenticated
    })


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
    
    return render(request, 'education/education_form.html', {'form': form, 'action': 'Add'})


@login_required
def edit_education(request, pk):
    """Edit education entry"""
    edu = get_object_or_404(Education, pk=pk)
    
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=edu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education updated successfully')
            return redirect('admin_dashboard')
    else:
        form = EducationForm(instance=edu)
    
    return render(request, 'education/education_form.html', {'form': form, 'action': 'Edit'})


@login_required
def delete_education(request, pk):
    """Delete education entry"""
    edu = get_object_or_404(Education, pk=pk)
    
    if request.method == 'POST':
        edu.delete()
        messages.success(request, 'Education deleted successfully')
        return redirect('admin_dashboard')
    
    return render(request, 'admin/confirm_delete.html', {
        'item': edu,
        'item_type': 'Education'
    })
