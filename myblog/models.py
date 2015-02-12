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

class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    title = models.CharField("Titile", max_length=128)
    user_id = models.ForeignKey(Users)
    content = models.TextField("Content")
    pub_data = models.DateTimeField(auto_now_add=True)
    edit_date=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s writed at %s"%(self.title,str(self.pub_date))
class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment=models.TextField("Comment")
    user_id=models.ForeignKey(Users)
    post_id=models.ForeignKey(Blog)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.comment

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    name=models.CharField("Category Name",max_length=64)
    #parent_id=models.IntegerField()
    parent_id=models.ForeignKey("self",blank=True)

    def __unicode__(self):
        return self.name

class Cat_Blog_Map(models.Model):
    map_id=models.AutoField(primary_key=True)
    blog_id=models.ForeignKey(Blog)
    cat_id=models.ForeignKey(Category)

class Images(models.Model):
    img_id=models.AutoField(primary_key=True)
    img_name=models.CharField("Image Name",max_length=64)
    img_url=models.CharField("Image URL",max_length=256)
    blog_id=models.ForeignKey(Blog)
   
    def __unicode__(self):
        return self.img_url
