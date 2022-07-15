from rest_framework import serializers
from authentication.serializers import *
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'writer': {
                'read_only': True
            }
        }

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['post', 'url']

class PostSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only = True)
    images = ImageSerializer(many = True, read_only = True)

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'likes': {
                'read_only': True
            }
        }