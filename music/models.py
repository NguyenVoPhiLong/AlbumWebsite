from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

# Album
class Album(models.Model):
    albumid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250,blank=True,null=True)
    logo = models.CharField(max_length=250,blank=True,null=True)
    star = models.CharField(max_length=250,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING, blank=True, null = True)  # <= Người tạo album

    def __str__(self):
        return self.title

class Song(models.Model):
    songid = models.AutoField(primary_key=True)
    albumid = models.ForeignKey(Album,on_delete=models.DO_NOTHING,blank=True, null=True)
    songname = models.CharField(max_length=250,blank=True,null=True)
    audio = models.CharField(max_length=250,blank=True,null=True)
    star = models.CharField(max_length=250,blank=True,null=True)

