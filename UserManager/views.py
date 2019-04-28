from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer


class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
