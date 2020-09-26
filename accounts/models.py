from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.utils.text import slugify
from django.urls import reverse


class Member(User, PermissionsMixin, models.Model):

    slug = models.SlugField(allow_unicode=True, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    about = models.TextField(max_length=1000)
    website = models.URLField(blank=True)


    def __str__(self):
        return "@{}".format(self.username)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"slug": self.slug})
    
