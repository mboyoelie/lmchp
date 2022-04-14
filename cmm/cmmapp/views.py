from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def reception(request):
    return render(request,'reception.html')

def triage(request):
    return render(request,'triage.html')

def consultations(request):
    return render(request,'consultations.html')
