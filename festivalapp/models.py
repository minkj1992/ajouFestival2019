from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField('title',max_length=100,default="")
    owner_name = models.CharField(max_length=20,default="")
    contents = models.TextField('contents')
    owner_pwd = models.CharField('password',max_length=8,default="")
    posted_date = models.DateTimeField('posted_date',auto_now_add=True)
    image_url = models.URLField('imageurl',max_length=1000,default="")
    image = models.FileField(null=True, blank=True)
    is_finish = models.IntegerField(default=0)

class Pub(models.Model):
    name = models.CharField('title',max_length=100,default="")
    description =  models.TextField('description')
    section = models.CharField(max_length = 2)
    location = models.CharField(max_length = 10)
    time = models.CharField(max_length = 10)
    # date = models.CharField(max_length = 10)
    # image_booth = models.FileField(null=True, blank=True)
    date1 = models.IntegerField(default=0)
    date2 = models.IntegerField(default=0)
    date3 = models.IntegerField(default=0)
    image_booth = models.URLField('imagebooth',max_length=1000,default="")

class Comment(models.Model):
    name = models.CharField(max_length=20,default="")
    contents = models.TextField('contents')
    pwd = models.CharField('password',max_length=8,default="")
    posted_date = models.DateTimeField('posted_date',auto_now_add=True)
    # commented_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    commented_post = models.IntegerField(default=0)

def __str__(self):
    return self.title 

