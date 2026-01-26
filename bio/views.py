from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bio
from .forms import BioForm


def home(request):
    """Home page with bio section"""
    bio = Bio.objects.first()
    return render(request, 'bio/index.html', {
        'bio': bio,
        'is_admin': request.user.is_authenticated
    })


@login_required
def edit_bio(request):
    """Edit or create bio"""
    bio = Bio.objects.first()
    
    if request.method == 'POST':
        form = BioForm(request.POST, instance=bio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bio updated successfully')
            return redirect('admin_dashboard')
    else:
        form = BioForm(instance=bio)
    
    return render(request, 'bio/bio_form.html', {'form': form})
