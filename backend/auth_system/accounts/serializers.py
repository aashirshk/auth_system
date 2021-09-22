from django.db.models.base import Model
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta:
        model = User,
        fields = ['id', 'email', 'name', 'password']