from django.db import models
from django.contrib.auth.models import User
import tinymce
from tinymce.models import HTMLField

# Create your models here.

class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=128, blank=True, null=True)
    author = models.ForeignKey('My_bbs_users',on_delete=models.CASCADE)
    view_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category = models.ForeignKey('Categories',on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Post_details(models.Model):
    id = models.IntegerField(primary_key=True)
    content = HTMLField(verbose_name='文章详情')
    post = models.OneToOneField('Posts',verbose_name="所属文章",on_delete=models.CASCADE)

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey('My_bbs_users',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    post = models.ForeignKey('Posts',on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class My_bbs_users(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    signature = models.CharField(max_length=128,default="这家伙也太懒了")
    headshow = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user0.png")
    def __str__(self):
        return self.user.username

class Categories(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    superadmin = models.CharField(max_length=32)
    admin = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name