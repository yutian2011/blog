# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField("User Name",max_length=32)
    passwd=models.CharField("User Passwd",max_length=64)
    email=models.EmailField()
    register_date=models.DateTimeField(auto_now_add=True)
    last_login_date=models.DateTimeField(auto_now=True)
    last_ip=models.CharField("User login ip address",max_length=32)
    def __unicode__(self):
        return "ID:%d User:%s Email:%s"%(user_id,user_name,email)
    

# Create your models here.

class Post(models.Model):
    title = models.CharField(u"标题", max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField(u"内容")
    pub_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'pk': self.pk})
