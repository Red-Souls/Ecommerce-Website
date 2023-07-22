from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 116)
    subTitle = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField(upload_to = 'blog')
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)