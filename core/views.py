from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def forbidden(request):
    return render(request, '403.html')
