from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, UserCreateSerializer
from .models import User



class AdminListUsers(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )

    def list(self):
        serializer = UserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            user.delete()
            content = {'User': 'has deleted'}
            return Response(content, status=HTTP_204_NO_CONTENT)
        else:
            users = User.objects.all()
            users.delete()
            content = {'Users': 'have deleted'}
            return Response(content, status=HTTP_204_NO_CONTENT)


class CurrentUser(generics.GenericAPIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        serializer = UserSerializer(get_object_or_404(User, username=request.user.username))
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(data=request.data, instance=get_object_or_404(User, username=request.user.username))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        user = get_object_or_404(User, username=request.user.username)
        user.delete()
        content = {'User': 'has deleted'}
        return Response(content, status=HTTP_204_NO_CONTENT)


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
