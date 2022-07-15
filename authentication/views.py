from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnOrReadOnly
from .serializers import *
from .models import *
from api.serializers import PostSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnOrReadOnly]

    @action(detail = True, methods = ['get'])
    def post(self, request, pk):
        posts = self.get_object().posts
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    @action(detail = True, methods = ['get', 'delete'], permission_classes = [IsAuthenticated])
    def follow(self, request, pk):
        user = self.get_object()
        if user == request.user:
            return Response({"message": "자기 자신은 팔로우할 수 없습니다."}, status = 400)
        if request.method == 'GET':
            user.followers.add(request.user)
        elif request.method == 'DELETE':
            user.followers.remove(request.user)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnOrReadOnly]
