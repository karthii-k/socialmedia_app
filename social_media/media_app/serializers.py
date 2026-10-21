from media_app.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        read_only_fields=['id']
    def create(self,validated__data):
            return User.objects.create_user(**validated__data)


class PostSerializer(serializers.ModelSerializer):
     total_like=serializers.SerializerMethodField()
     total_comment=serializers.SerializerMethodField()
     class Meta:
          model=Post
          fields='__all__'
          read_only_fields=['created_at','owner']

     def get_total_like(self,object):
        post1=Like.objects.filter(post_obj=object)
        return post1.count()

     def get_total_comment(self,object):
        no_comment=Comment.objects.filter(post_obj=object)
        return no_comment.count()

class CommentSerializer(serializers.ModelSerializer):
     class Meta:
          model=Comment
          fields='__all__'
          read_only_fields=['owner','added_at']

          

class LikeSerializer(serializers.ModelSerializer):
     class Meta:
          model=Like
          fields='__all__'
          read_only_fields=['id','owner_obj','created_at']


