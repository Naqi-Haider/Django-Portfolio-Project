from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'education.html')

def skills(request):
    return render(request, 'skills.html')

def experience(request):
    return render(request, 'experience.html')
