from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Posts",null=True)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Comments')
    post_obj=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='Comments')

    def __str__(self):
        return  self.comment


class Like(models.Model):
    post_obj=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    owner_obj=models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('owner_obj','post_obj')


