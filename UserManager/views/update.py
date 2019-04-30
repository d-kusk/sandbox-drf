from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from django.contrib.auth import get_user_model
from UserManager.serializers import UserSerializer

User = get_user_model()


class UserUpdateView(UpdateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
