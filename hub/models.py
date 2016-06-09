from __future__ import unicode_literals

from django.db import models

# Create your models here.

def upload_path_handler(instance, filename):
    print("INSTANCE: " + instance.user_belongs)
    print("FILENAME: " + filename)
    return "uploads/{id}/{commit_id}/{file}".format(id=instance.user_belongs, commit_id=instance.commit_id, file=filename)
    
class File(models.Model):
    name = models.CharField(max_length=30)
    user_belongs = models.CharField(max_length=30)
    commit_id = models.CharField(max_length=30)
    file = models.FileField(upload_to=upload_path_handler)