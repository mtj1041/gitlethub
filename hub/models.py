from __future__ import unicode_literals

from django.db import models

# Create your models here.

class File(models.Model):
    commit_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    user_belongs = models.CharField(max_length=30)
    file = models.FileField(upload_to='uploads/' + user_belongs + '/' + commit_id)