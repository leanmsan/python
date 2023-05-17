from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout # type: ignore
from django.http import HttpRequest, HttpResponse

# Create your views here.
@login_required
def index(request):
    return render(request, 'registration/login.html', {})

def logout(request):
    logout(request)
    return redirect('/')
