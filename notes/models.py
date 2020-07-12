#!/usr/bin/env python3
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from ckeditor.fields import RichTextField


class Notes(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(
        User, default=None, blank=True, related_name="notes_likes")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=25, default="CS") 
    slug = models.SlugField(null = True, unique = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        uniqueid = get_random_string(length = 64)
        self.slug = slugify(uniqueid)
        super().save(*args, **kwargs)
