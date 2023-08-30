from django.shortcuts import render

# Create your views here.

def Login_shower(request):
    return render(request, 'Login.html')
