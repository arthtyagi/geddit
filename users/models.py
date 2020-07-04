from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img.save(self.image.path, quality=90)

        if img.height > 300 and img.width < 300:
            output_size = (img.width, img.width)
            img = img.resize((img.width, img.width), Image.ANTIALIAS)
            img.save(self.image.path, quality=90)

        if img.height < 300 and img.width > 300:
            output_size = (img.height, img.height)
            img = img.resize((img.height, img.height), Image.ANTIALIAS)
            img.save(self.image.path, quality=90)
