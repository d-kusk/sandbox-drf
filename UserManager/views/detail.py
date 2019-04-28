from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from django.contrib.auth import get_user_model
from UserManager.serializers import UserSerializer

User = get_user_model()


class UserDetailView(RetrieveModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
