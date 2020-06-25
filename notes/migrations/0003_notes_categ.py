# Generated by Django 3.0.7 on 2020-06-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='categ',
            field=models.CharField(choices=[('M', 'Mathematics'), ('P', 'Physics'), ('C', 'Chemistry'), ('CS', 'Computer Science')], default='CS', max_length=55),
        ),
    ]