from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import *
from .serializers import *
from .models import *

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)
        post = Post.objects.get(id = serializer.data['id'])
        images = self.request.FILES.getlist('images')
        for image in images:
            Image.objects.create(post = post, url = image)

    @action(detail = True, methods = ['get'])
    def comment(self, request, pk):
        comments = Post.objects.get(id = pk).comments
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)

    @action(detail = True, methods = ['get', 'delete'])
    def like(self, request, pk):
        post = self.get_object()
        if request.method == "GET":
            post.like.add(request.user)
        elif request.method == "DELETE":
            post.like.remove(request.user)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)