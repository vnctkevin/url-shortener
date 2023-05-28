from django.shortcuts import render
from django.http import HttpResponse
from .models import Link
from django.shortcuts import redirect
from .forms import LinkForm

# Create your views here.
def shorten_link(request):
    form = LinkForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'index.html', {'form': form, 'shortUrl': form.cleaned_data['shortUrl']})
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def redirect_link(request, shortUrl):
    try:
        link = Link.objects.get(shortUrl=shortUrl)
        return redirect(link.longUrl)
    except:
        return HttpResponse('Link not found')

