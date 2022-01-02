from django.db.models import fields
from rest_framework import serializers
from .models import Room, Message
from datetime import datetime
class GetAllMessage(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','value','date','user','room')
    
class MessageSerializers(serializers.Serializer):
    value = serializers.CharField(max_length=1000000)
    date = serializers.DateTimeField()
    user = serializers.CharField(max_length=1000000)
    room = serializers.CharField(max_length=255)


