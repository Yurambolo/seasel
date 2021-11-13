from django.urls import path
from .views import AdministratorObtainTokenPairView, AdministratorRegisterView, StudentObtainTokenPairView, \
    StudentRegisterView, TeacherObtainTokenPairView, TeacherRegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('administrator/login/', AdministratorObtainTokenPairView.as_view()),
    path('administrator/login/refresh/', TokenRefreshView.as_view()),
    path('administrator/register/', AdministratorRegisterView.as_view()),
    path('student/login/', StudentObtainTokenPairView.as_view()),
    path('student/login/refresh/', TokenRefreshView.as_view()),
    path('student/register/', StudentRegisterView.as_view()),
    path('teacher/login/', TeacherObtainTokenPairView.as_view()),
    path('teacher/login/refresh/', TokenRefreshView.as_view()),
    path('teacher/register/', TeacherRegisterView.as_view()),
    # path('test/', ExampleView.as_view())
]
