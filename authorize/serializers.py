import json

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Administrator, Student, Teacher

class TeacherTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Teacher.USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super(TeacherTokenObtainPairSerializer, cls).get_token(user)

        # token['email'] = user.email
        # token['name'] = user.name
        return token

    def validate(self, attrs):
        try:
            request = self.context["request"]
        except KeyError:
            pass

        try:
            data = {}
            request_data = request.data
            if ("email" in request_data and "password" in request_data):
                user = Teacher.objects.filter(email=request_data['email']).first()
                if user.check_password(request_data['password']):
                    self.user = user
            else:
                raise serializers.ValidationError({"username/password": "These fields are required"})


            refresh = self.get_token(self.user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            return data

        except:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

class AdministratorTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Administrator.USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super(AdministratorTokenObtainPairSerializer, cls).get_token(user)

        # token['email'] = user.email
        # token['name'] = user.name
        return token

    def validate(self, attrs):
        try:
            request = self.context["request"]
        except KeyError:
            pass

        try:
            data = {}
            request_data = request.data
            if ("email" in request_data and "password" in request_data):
                user = Administrator.objects.filter(email=request_data['email']).first()
                if user.check_password(request_data['password']):
                    self.user = user
            else:
                raise serializers.ValidationError({"username/password": "These fields are required"})


            refresh = self.get_token(self.user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            return data

        except:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

class StudentTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Student.USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super(StudentTokenObtainPairSerializer, cls).get_token(user)

        # token['email'] = user.email
        # token['name'] = user.name
        return token

    def validate(self, attrs):
        try:
            request = self.context["request"]
        except KeyError:
            pass

        try:
            data = {}
            request_data = request.data
            if ("email" in request_data and "password" in request_data):
                user = Student.objects.filter(email=request_data['email']).first()
                if user.check_password(request_data['password']):
                    self.user = user
            else:
                raise serializers.ValidationError({"username/password": "These fields are required"})


            refresh = self.get_token(self.user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            return data

        except:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )


class AdministratorRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Administrator.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Administrator
        fields = ('email', 'password', 'password2', 'name', 'music_school')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        if 'company' not in validated_data:
            validated_data['company'] = None
        if 'gender' not in validated_data:
            validated_data['gender'] = None
        user = Administrator.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            music_school_id=validated_data['music_school'].id,
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class StudentRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Student
        fields = ('email', 'password', 'password2', 'name', 'music_school')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        if 'company' not in validated_data:
            validated_data['company'] = None
        if 'gender' not in validated_data:
            validated_data['gender'] = None
        user = Student.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            music_school_id=validated_data['music_school'].id,
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class TeacherRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Teacher.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Teacher
        fields = ('email', 'password', 'password2', 'name', 'music_school')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        if 'company' not in validated_data:
            validated_data['company'] = None
        if 'gender' not in validated_data:
            validated_data['gender'] = None
        user = Teacher.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            music_school_id=validated_data['music_school'].id,
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
