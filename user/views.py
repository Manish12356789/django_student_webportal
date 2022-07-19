from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Student.decorators import unauthenticated_user
from django.contrib.auth import authenticate, login as auth_login, logout as dj_logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User

@unauthenticated_user
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=User.objects.get(email=username), password=password)
        except:
            user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('students/')

        else:
            messages.info(request, 'Invalid Username or password')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    dj_logout(request)
    return redirect('login')