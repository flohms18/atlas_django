from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Tag (models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
            return self.name

class Post(models.Model):
    title = models.CharField(max_length=300,null=False)
    slug = models.SlugField(unique=True,null=False)
    content = HTMLField()
    published_date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
