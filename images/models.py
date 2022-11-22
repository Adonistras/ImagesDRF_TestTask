from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Image(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{datetime.now()}')
        super().save(*args, **kwargs)
