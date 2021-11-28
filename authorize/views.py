from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserTokenObtainPairSerializer, AdministratorRegisterSerializer, StudentRegisterSerializer, \
    TeacherRegisterSerializer


class UserObtainTokenPairView(TokenObtainPairView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserTokenObtainPairSerializer


class AdministratorRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AdministratorRegisterSerializer


class StudentRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = StudentRegisterSerializer


class TeacherRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TeacherRegisterSerializer
