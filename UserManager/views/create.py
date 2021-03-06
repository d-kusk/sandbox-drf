from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from UserManager.serializers import UserSerializer

User = get_user_model()


class UserCreateView(CreateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
