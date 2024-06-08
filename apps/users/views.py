from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users.models import Users
from apps.users.serializeers import UsersSerializer

class UsersAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
