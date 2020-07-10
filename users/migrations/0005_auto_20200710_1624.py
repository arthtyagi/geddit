# Generated by Django 3.0.8 on 2020-07-10 10:54

import awesome_avatar.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200709_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=awesome_avatar.fields.AvatarField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]