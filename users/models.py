from django.db import models
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse_lazy
from django.utils.text import slugify 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics/', validators=[validate_image_file_extension])
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse_lazy('users:profilepage', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        username = self.user.username
        self.slug = slugify(username)
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 500 and img.width > 500:
            img = img.resize((500, 500), Image.ANTIALIAS)
            img.save(self.image.path, quality=90)

        if img.height > 500 and img.width < 500:
            img = img.resize((img.width, img.width), Image.ANTIALIAS)
            img.save(self.image.path, quality=90)

        if img.height < 500 and img.width > 500:
            img = img.resize((img.height, img.height), Image.ANTIALIAS)
            img.save(self.image.path, quality=90)
