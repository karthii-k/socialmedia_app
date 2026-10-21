from django.shortcuts import render
# from django.views.generic import UpdateView
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from media_app.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class AddUser(CreateAPIView):
    serializer_class=UserSerializer


class UserPostView(CreateAPIView,RetrieveAPIView):
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Post.objects.all()

    def perform_create(self,serializer):
          return serializer.save(owner=self.request.user)

    def show_post(self):
         return self.queryset.filter(owner=self.request.user)

class UserPostRetreiveView(UpdateAPIView,DestroyAPIView):
     serializer_class=PostSerializer
     authentication_classes=[TokenAuthentication]
     permission_classes=[IsAuthenticated]
     queryset=Post.objects.all()

class CommentView(CreateAPIView,ListAPIView):
     serializer_class=CommentSerializer
     authentication_classes=[TokenAuthentication]
     permission_classes=[IsAuthenticated]
     queryset=Comment.objects.all()

     def perform_create(self,serializer):
          post = serializer.validated_data['post_obj']
          serializer.save(owner=post.owner)

class LikeView(CreateAPIView):
     serializer_class=LikeSerializer
     authentication_classes=[TokenAuthentication]
     permission_classes=[IsAuthenticated]

     def perform_create(self, serializer):
         serializer.save(owner_obj=self.request.user)

     