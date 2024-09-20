import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_tracker.settings')

from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Meal
from .forms import MealForm  # We will create MealForm next

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('meals')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('meals')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def meals_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MealForm(request.POST)
            if form.is_valid():
                meal = form.save(commit=False)
                meal.user = request.user
                meal.save()
                return redirect('meals')
        else:
            form = MealForm()
        meals = Meal.objects.filter(user=request.user)
        return render(request, 'meals.html', {'meals': meals, 'form': form})
    return redirect('login')