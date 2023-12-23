from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

