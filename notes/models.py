#!/usr/bin/env python3
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Notes(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=25, default="CS")
    image = models.ImageField(null=True, blank=True,
                              default="default.jpg", upload_to='notes_pics/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Notes, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
