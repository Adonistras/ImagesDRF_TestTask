from django.urls import path
from .views import CreateImageAPI, DetailImage, ListImages, DetailReadImage


urlpatterns = [
    path('', ListImages.as_view(), name='list-images'),
    path('<slug:slug>/', DetailReadImage.as_view(), name='retrieve-image'),
    path('<slug:slug>/update', DetailImage.as_view(), name='update-image'),
    path('<slug:slug>/delete', DetailImage.as_view(), name='delete-image'),
    path('create/', CreateImageAPI.as_view(), name='create-image'),
    ]