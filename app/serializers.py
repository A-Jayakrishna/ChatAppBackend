from rest_framework import serializers
from .models import User,Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=['sender','msg','time']
