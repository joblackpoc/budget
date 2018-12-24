
from django.shortcuts import render

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    # fetch the correct project
    return render(request, 'budget/project-detail.html')
