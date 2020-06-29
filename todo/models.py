from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

class Todo(models.Model):
	title = encrypt(models.CharField(max_length=350))
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = encrypt(models.CharField(max_length=550))
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('todo:detail', kwargs={'pk': self.pk})
