from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from api.models import *
from rest_framework import serializers


class MusicSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicSchool
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=False, allow_blank=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password2', 'name', 'music_school', 'role')
        extra_kwargs = {
            'name': {'required': True},
            'music_school': {'required': True},
            'role': {'required': True},
        }

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        representation['music_school'] = MusicSchoolSerializer(instance.music_school).data
        return representation

    def validate(self, attrs):
        if 'password' in attrs and attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def update(self, instance, validated_data):
        if 'email' in validated_data:
            instance.email = validated_data['email']
        if 'name' in validated_data:
            instance.name = validated_data['name']
        if 'music_school' in validated_data:
            instance.music_school = validated_data['music_school']
        if 'role' in validated_data:
            instance.role = validated_data['role']
        if 'password' in validated_data and validated_data['password']:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            music_school=validated_data['music_school'],
            role=validated_data['role'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class SemesterSerializer(serializers.ModelSerializer):
    music_school = MusicSchoolSerializer(many=False, read_only=True)

    class Meta:
        model = Semester
        fields = ['id', 'music_school', 'number', 'composition_count', 'max_difficulty', 'min_difficulty']

    def to_representation(self, instance):
        representation = super(SemesterSerializer, self).to_representation(instance)
        representation['music_school'] = MusicSchoolSerializer(instance.music_school).data
        return representation


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name']


class ConcertSerializer(serializers.ModelSerializer):
    # music_school = MusicSchoolSerializer(many=False, read_only=True)

    class Meta:
        model = Concert
        fields = ['id', 'music_school', 'date']

    def to_representation(self, instance):
        representation = super(ConcertSerializer, self).to_representation(instance)
        representation['music_school'] = MusicSchoolSerializer(instance.music_school).data
        return representation


class CompositionSerializer(serializers.ModelSerializer):
    instrument = InstrumentSerializer(many=False, read_only=True)

    class Meta:
        model = Composition
        fields = ['id', 'name', 'instrument', 'author', 'difficulty']

    def to_representation(self, instance):
        representation = super(CompositionSerializer, self).to_representation(instance)
        representation['instrument'] = InstrumentSerializer(instance.instrument).data
        return representation


class CompositionRepresentationSerializer(serializers.ModelSerializer):
    # composition = CompositionSerializer(many=False, read_only=True)

    class Meta:
        model = CompositionRepresentation
        fields = ['id', 'composition', 'format', 'sheme']

    def to_representation(self, instance):
        representation = super(CompositionRepresentationSerializer, self).to_representation(instance)
        representation['composition'] = CompositionSerializer(instance.composition).data
        return representation


class CourseSerializer(serializers.ModelSerializer):
    # student = UserSerializer(many=False, read_only=True)
    # teacher = UserSerializer(many=False, read_only=True)
    # semester = SemesterSerializer(many=False, read_only=True)
    # instrument = InstrumentSerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'student', 'teacher', 'semester', 'instrument']

    def to_representation(self, instance):
        representation = super(CourseSerializer, self).to_representation(instance)
        representation['student'] = UserSerializer(instance.student).data
        representation['teacher'] = UserSerializer(instance.teacher).data
        representation['semester'] = SemesterSerializer(instance.semester).data
        representation['instrument'] = InstrumentSerializer(instance.instrument).data
        return representation


class ProgramSerializer(serializers.ModelSerializer):
    # concert = ConcertSerializer(many=False, read_only=True)
    # course = CourseSerializer(many=False, read_only=True)
    # semester = SemesterSerializer(many=False, read_only=True)
    # compositions = CompositionSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = ['id', 'concert', 'course', 'semester']

    def to_representation(self, instance):
        representation = super(ProgramSerializer, self).to_representation(instance)
        representation['concert'] = ConcertSerializer(instance.concert).data
        representation['course'] = CourseSerializer(instance.course).data
        representation['semester'] = SemesterSerializer(instance.semester).data
        return representation


class RepetitionSerializer(serializers.ModelSerializer):
    # course = CourseSerializer(many=False, read_only=True)
    # composition = CompositionSerializer(many=False, read_only=True)

    class Meta:
        model = Repetition
        fields = ['id', 'course', 'composition', 'datetime', 'mark']

    def to_representation(self, instance):
        representation = super(RepetitionSerializer, self).to_representation(instance)
        representation['composition'] = CompositionSerializer(instance.composition).data
        representation['course'] = CourseSerializer(instance.course).data
        return representation


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'composition', 'mark', 'comment', 'created_at']

    def to_representation(self, instance):
        representation = super(FeedbackSerializer, self).to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['composition'] = CompositionSerializer(instance.composition).data
        return representation