from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Link, Microsite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LinkForm, MicrositeForm

@login_required
def dashboard(request):
    user_links = Link.objects.filter(user=request.user)
    user_microsites = Microsite.objects.filter(user=request.user)
    context = {
        'links': user_links,
        'microsites': user_microsites
    }
    return render(request, 'dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
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
    return render(request, 'index.html', context)

def redirect_link(request, shortUrl):
    try:
        link = Link.objects.get(shortUrl=shortUrl)
        link.clicks += 1
        link.save()
        return redirect(link.longUrl)
    except:
        return HttpResponse('Link not found')
