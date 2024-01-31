from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . models import Profile, WorkExperience
from .forms import WorkExperienceForm, ProfileForm
from django.views.generic.edit import CreateView, UpdateView


def home(request):
    return render(request, 'home.html')

def about_me(request):
    return render(request, 'about_me.html')

def profile(request):
    return render(request, 'profile.html')

def profile_1(request):
    my_profile, created = Profile.objects.get_or_create(id=1)
    # Pass the profile instance to the template
    context = {'profile': my_profile}
    return render(request, 'profile_1.html', context)

@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(id=1)  # Assuming the profile has id=1

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_1')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'form': form})


@login_required
def add_work_experience(request):
    profile, created = Profile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience_instance = form.save()
            profile.work_experiences.add(work_experience_instance)
            return redirect('profile_1')
    else:
        form = WorkExperienceForm()

    return render(request, 'add_work_experience.html', {'form': form})

@login_required
def update_work_experience(request, pk):
    profile, created = Profile.objects.get_or_create(id=1)
    
    # Ensure the work_experience_instance is related to the profile
    work_experience_instance = profile.work_experiences.get(pk=pk)

    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience_instance)
        if form.is_valid():
            form.save()
            return redirect('profile_1')
    else:
        form = WorkExperienceForm(instance=work_experience_instance)

    return render(request, 'update_work_experience.html', {'form': form})