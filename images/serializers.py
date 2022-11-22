from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('name', 'description', 'created', 'url', 'owner', 'slug')


class ImageCreateSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Image
        fields = ('name', 'description', 'url', 'slug')

