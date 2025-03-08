from django.contrib import admin
from django.db import models
from url.models import Microsite
from martor.widgets import AdminMartorWidget
# Register your models here.

class MicrositeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Microsite, MicrositeAdmin)