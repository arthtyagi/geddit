from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
from django.urls import reverse
# Create your models here.


class Query(models.Model):


class Answer(models.Model):



def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]