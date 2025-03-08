from django.db import models
from django.contrib.auth.models import User
from martor.models import MartorField  # For Markdown support

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    longUrl = models.URLField()
    shortUrl = models.CharField(max_length=10, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  # Changed from auto_now_add to auto_now
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.shortUrl

class Microsite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = MartorField()  # Changed to MartorField for Markdown support
    content = MartorField()      # Added MartorField for Markdown support
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  # Changed from auto_now_add to auto_now
    links = models.ManyToManyField(Link)

    def __str__(self):
        return self.name