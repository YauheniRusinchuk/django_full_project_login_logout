from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(blank=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return str(self.avatar)

    class Meta:
        verbose_name = "Profile"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    content = models.TextField(blank=False)
    img = models.FileField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        ordering = ["-date"]



class Comment(models.Model):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text
