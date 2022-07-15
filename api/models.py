from django.db import models
from django.conf import settings

class PostForm(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = '%(class)ss', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'liked_%(class)s', blank = True)

    class Meta :
        abstract = True

class Post(PostForm):
    pass

class Comment(PostForm):
    post = models.ForeignKey(Post, related_name = '%(class)ss', on_delete = models.CASCADE)

class Image(models.Model):
    post = models.ForeignKey(Post, related_name = '%(class)ss', on_delete = models.CASCADE)
    url = models.ImageField(upload_to = 'post/')