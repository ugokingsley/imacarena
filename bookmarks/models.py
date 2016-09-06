from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Link(models.Model):
    url = models.URLField(unique=True)

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username
