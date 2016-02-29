from django.db import models

# Create your models here.
class Quote(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
