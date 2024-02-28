from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def register(request):

    return render(request, 'regester.html')

def my_login(request):

    return render(request, 'mylogin.html')

def dashboard(request):

    return render(request, 'dashboard.html')

def profile_management(request):

    return render(request, 'profile-management.html')