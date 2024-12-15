import datetime
from rest_framework import serializers

from taggit.serializers import TaggitSerializer, TagListSerializerField

from images.models import Image

class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    username = serializers.SerializerMethodField()
    image_url = serializers.URLField(source='get_image_url')

    timestamp = serializers.SerializerMethodField()
    
    class Meta:
        model = Image
        fields = ['username', 'name', 'image_url', 'tags', 'timestamp']

    def get_username(self, obj):
        username = obj.user.get_full_name() or obj.user.username
        return username
    
    def get_timestamp(self, obj):
        
        date = obj.timestamp.strftime("%d/%m/%Y, %H:%M:%S")
        return date # time format 08/12/2024, 19:50:23