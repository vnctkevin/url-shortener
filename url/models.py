from django.db import models

# Create your models here.
class Link(models.Model):
    longUrl = models.URLField()
    shortUrl = models.CharField(max_length=10, unique=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.shortUrl