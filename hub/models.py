from __future__ import unicode_literals

from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    name = models.CharField(max_length=30)
    user_belongs = models.CharField(max_length=30)