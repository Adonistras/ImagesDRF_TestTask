from django.urls import path, include
from rest_framework import routers
from .views import AdminListUsers, CreateUser, CurrentUser

router = routers.DefaultRouter()
router.register(r'admin', AdminListUsers)

urlpatterns = [
    path('', include(router.urls)),
    path('myprofile/', CurrentUser.as_view(), name='users-profile'),
    path('create/', CreateUser.as_view(), name='create-user'),
]