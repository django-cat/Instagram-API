from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data): 
        super().update(instance, validated_data)
        if('password' in validated_data):
            instance.set_password(validated_data['password'])
            instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'followers']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'email': {
                'write_only': True
            },
        }

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
