from rest_framework import generics
from .serializers import ImageSerializer, ImageCreateSerializer
from .models import Image
from users.permissions import IsYourProfile
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ListImages(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated, )


class DetailReadImage(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated, )


class CreateImageAPI(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageCreateSerializer
    permission_classes = (IsAuthenticated, )


class DetailImage(generics.UpdateAPIView, generics.DestroyAPIView):
    lookup_field = 'slug'
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsYourProfile, )



