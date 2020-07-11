from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


class Query(models.Model):
    title = models.CharField(max_length=240)
    user = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL)
    content = RichTextField(null=True, blank=True)
    likes = models.ManyToManyField(
        User, default=None, blank=True, related_name="query_likes")
    category = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.name = self.user.username
        super(Query, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    user = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, default=None, blank=True, related_name="answer_likes")

    def save(self, *args, **kwargs):
        if not self.id:
            self.name = self.user.username
        super(Answer, self).save(*args, **kwargs)
