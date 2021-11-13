from api.models import *
from authorize.models import Administrator
from rest_framework import serializers


class MusicSchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicSchool
        fields = ['name']


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ['email', 'name', 'music_school']


class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = ['email', 'name', 'music_school']


class AdministratorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Administrator
        fields = ['email', 'name', 'music_school']


class SemesterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Semester
        fields = ['music_school', 'number', 'composition_count', 'max_difficulty', 'min_difficulty']


class InstrumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Instrument
        fields = ['name']


class ConcertSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Concert
        fields = ['music_school', 'date']


class CompositionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Composition
        fields = ['name', 'instrument', 'author', 'difficulty']


class CompositionRepresentationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CompositionRepresentation
        fields = ['composition', 'format', 'sheme']


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ['student', 'teacher', 'semester', 'instrument']


class ProgramSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Program
        fields = ['concert', 'course', 'semester', 'compositions']


class RepetitionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Repetition
        fields = ['course', 'composition', 'datetime', 'mark']

