from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

ROLE_CHOICES = [('ADMIN', 'ADMIN'), ('TEACHER', 'TEACHER'), ('STUDENT', 'STUDENT')]


class MusicSchool(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, music_school=None):
        if name is None:
            raise TypeError('Users should have a name')
        if music_school is None:
            raise TypeError('Users should have a music school')
        if email is None:
            raise TypeError('Users should have an Email')

        user = self.model(email=self.normalize_email(email), name=name, music_school_id=music_school)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password=None, music_school=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, name, password, music_school)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    music_school = models.ForeignKey(MusicSchool, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)

    user_permissions = None
    groups = None
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'music_school', 'role']

    objects = UserManager()

    def __str__(self):
        return self.name

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


# class Administrator(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     music_school = models.ForeignKey(MusicSchool, on_delete=models.CASCADE)
#
#     user_permissions = None
#     groups = None
#     is_staff = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'music_school']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.name
#
#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
#
#
# class Student(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     music_school = models.ForeignKey(MusicSchool, on_delete=models.CASCADE)
#
#     user_permissions = None
#     groups = None
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'music_school']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.name
#
#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
#
#
# class Teacher(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     music_school = models.ForeignKey(MusicSchool, on_delete=models.CASCADE)
#
#     user_permissions = None
#     groups = None
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'music_school']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.name
#
#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
