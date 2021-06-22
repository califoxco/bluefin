import uuid

from django.db import models

# Create your models here.
from django.utils.text import slugify


class Property(models.Model):
    propertyID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    slug = models.SlugField(default='0')
    listed_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
