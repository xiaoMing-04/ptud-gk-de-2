from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib.auth import logout
from blog.models import Task
from django.utils.timezone import now

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    overdue_tasks = Task.objects.filter(
        user=request.user,
        finished__lt=now(),
    ).exclude(status='C')
    overdue_count = overdue_tasks.count()

    overdue_tasks.update(status='O')
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'form': form,
        'overdue_count': overdue_count
    }
    return render(request, 'users/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')