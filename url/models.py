from django.db import models
from django.contrib.auth.models import User
from martor.models import MartorField  # For Markdown support
from django.dispatch import receiver
from django.db.models.signals import post_save

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
    slug = models.SlugField(unique=True)  # New field
    name = models.CharField(max_length=100)
    description = MartorField()  # Changed to MartorField for Markdown support
    content = MartorField()      # Added MartorField for Markdown support
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  # Changed from auto_now_add to auto_now
    links = models.ManyToManyField(Link)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Signal to create/update profile when user is created/updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()