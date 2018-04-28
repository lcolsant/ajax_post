# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validate(self, request):
        errors = False
        return errors

class Post(models.Model):
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return "<User object: {}>".format(self.post)
