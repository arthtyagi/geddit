from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import default_app_config, get_user_model
from django.utils import timezone
import datetime
from django.urls import reverse
from djangotoolbox.fields import ListField
from ckeditor.fields import RichTextField


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Query(models.Model):
    title = models.CharField(max_length=240)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET(get_sentinel_user()))
    content = models.RichTextField(null=True, blank=True)
    category = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    answers = models.IntegerField(default=0)
    likes = models.ManyToManyField(
        User, default=None, blank=True, related_name="query_likes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET(get_sentinel_user))
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    content = models.RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True
    likes = models.ManyToManyField(
        User, default=None, blank=True, related_name="query_likes")
