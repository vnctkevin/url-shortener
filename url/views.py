from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Link, Microsite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LinkForm, MicrositeForm, UserRegistrationForm, ProfileForm

@login_required
def dashboard(request):
    user_links = Link.objects.filter(user=request.user)
    user_microsites = Microsite.objects.filter(user=request.user)
    context = {
        'links': user_links,
        'microsites': user_microsites
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Update profile
            user.profile.first_name = form.cleaned_data['first_name']
            user.profile.last_name = form.cleaned_data['last_name']
            user.profile.email = form.cleaned_data['email']
            user.profile.date_of_birth = form.cleaned_data['date_of_birth']
            user.profile.phone_number = form.cleaned_data['phone_number']
            user.profile.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def shorten_link(request):
    form = LinkForm(request.POST or None)
    if form.is_valid():
        link = form.save(commit=False)
        link.user = request.user
        link.save()
        return render(request, 'index.html', {'form': form, 'shortUrl': link.shortUrl})
    context = {
        'form': form
    }
    return render(request, 'create-link.html', context)

def redirect_link(request, shortUrl):
    try:
        link = Link.objects.get(shortUrl=shortUrl)
        link.clicks += 1
        link.save()
        return redirect(link.longUrl)
    except:
        return HttpResponse('Link not found')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'profile.html', {'form': form})


@login_required
def create_microsite(request):
    if request.method == 'POST':
        form = MicrositeForm(request.POST)
        if form.is_valid():
            microsite = form.save(commit=False)
            microsite.user = request.user
            microsite.save()
            form.save_m2m()  # Save ManyToMany relationships
            messages.success(request, 'Microsite created successfully!')
            return redirect('dashboard')
    else:
        form = MicrositeForm()
    return render(request, 'microsites/create-microsite.html', {'form': form})

@login_required
def view_microsite(request, slug):
    microsite = get_object_or_404(Microsite, slug=slug)
    return render(request, 'microsites/view_microsite.html', {'microsite': microsite})

@login_required
def edit_microsite(request, pk):
    microsite = get_object_or_404(Microsite, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MicrositeForm(request.POST, instance=microsite)
        if form.is_valid():
            form.save()
            messages.success(request, 'Microsite updated successfully!')
            return redirect('dashboard')
    else:
        form = MicrositeForm(instance=microsite)
    return render(request, 'microsites/edit-microsite.html', {'form': form, 'microsite': microsite})

@login_required
def delete_microsite(request, pk):
    microsite = get_object_or_404(Microsite, pk=pk, user=request.user)
    if request.method == 'POST':
        microsite.delete()
        messages.success(request, 'Microsite deleted successfully!')
        return redirect('dashboard')
    return render(request, 'microsites/delete-microsite.html', {'microsite': microsite})