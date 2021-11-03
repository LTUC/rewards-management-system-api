from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer
from .permissions import AdminOnly, RecordOwner
# Create your views here.



class UserListView(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[AdminOnly]

class UserCreateView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    permission_classes=[RecordOwner]
