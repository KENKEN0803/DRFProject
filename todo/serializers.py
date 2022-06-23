from rest_framework import serializers
from .models import TodoList
from django.contrib.auth.models import User, Group


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('pk', 'author', 'contents', 'completed', 'writtenTime')
        exclude = ()


# 유저 관련
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
