from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=9, choices=Roles.choices)
    image_path = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=80)
    is_blocked = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Page(models.Model):
    name = models.CharField(max_length=80)
    uuid = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='pages')

    owner = models.ForeignKey('User', on_delete=models.CASCADE, related_name='pages')
    followers = models.ManyToManyField('User', related_name='requests')

    unblock_date = models.DateTimeField(null=True, blank=True)
