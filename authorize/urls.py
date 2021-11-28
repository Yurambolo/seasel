from django.urls import path
from .views import UserObtainTokenPairView, AdministratorRegisterView, StudentRegisterView, TeacherRegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', UserObtainTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/administrator/', AdministratorRegisterView.as_view()),
    path('register/student/', StudentRegisterView.as_view()),
    path('register/teacher/', TeacherRegisterView.as_view()),
]
