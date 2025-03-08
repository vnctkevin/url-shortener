from django import forms
from martor.fields import MartorFormField
from .models import Link, Microsite

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['longUrl', 'shortUrl']
        labels = {
            'longUrl': 'URL to shorten',
            'shortUrl': 'New Short URL'
        }
        widgets = {
            'longUrl': forms.URLInput(attrs={'class': 'form-control'})
        }

class MicrositeForm(forms.ModelForm):
    description = MartorFormField()
    content = MartorFormField()

    class Meta:
        model = Microsite
        fields = ['name', 'description', 'content', 'links']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'links': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
