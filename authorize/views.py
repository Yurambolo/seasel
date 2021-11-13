from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Administrator, Student, Teacher
from .serializers import StudentTokenObtainPairSerializer, AdministratorTokenObtainPairSerializer, \
    TeacherTokenObtainPairSerializer, AdministratorRegisterSerializer, StudentRegisterSerializer, \
    TeacherRegisterSerializer


class AdministratorObtainTokenPairView(TokenObtainPairView):
    queryset = Administrator.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AdministratorTokenObtainPairSerializer


class AdministratorRegisterView(generics.CreateAPIView):
    queryset = Administrator.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AdministratorRegisterSerializer


class StudentObtainTokenPairView(TokenObtainPairView):
    queryset = Student.objects.all()

    permission_classes = (AllowAny,)
    serializer_class = StudentTokenObtainPairSerializer


class StudentRegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = StudentRegisterSerializer


class TeacherObtainTokenPairView(TokenObtainPairView):
    queryset = Teacher.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TeacherTokenObtainPairSerializer


class TeacherRegisterView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TeacherRegisterSerializer
