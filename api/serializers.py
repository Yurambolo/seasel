from api.models import *
from rest_framework import serializers


class MusicSchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicSchool
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    music_school = MusicSchoolSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'music_school', 'role']


class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    music_school = MusicSchoolSerializer(many=False, read_only=True)

    class Meta:
        model = Semester
        fields = ['music_school', 'number', 'composition_count', 'max_difficulty', 'min_difficulty']


class InstrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrument
        fields = ['name']


class ConcertSerializer(serializers.HyperlinkedModelSerializer):
    music_school = MusicSchoolSerializer(many=False, read_only=True)

    class Meta:
        model = Concert
        fields = ['music_school', 'date']


class CompositionSerializer(serializers.HyperlinkedModelSerializer):
    instrument = InstrumentSerializer(many=False, read_only=True)

    class Meta:
        model = Composition
        fields = ['name', 'instrument', 'author', 'difficulty']


class CompositionRepresentationSerializer(serializers.HyperlinkedModelSerializer):
    composition = CompositionSerializer(many=False, read_only=True)

    class Meta:
        model = CompositionRepresentation
        fields = ['composition', 'format', 'sheme']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    student = UserSerializer(many=False, read_only=True)
    teacher = UserSerializer(many=False, read_only=True)
    semester = SemesterSerializer(many=False, read_only=True)
    instrument = InstrumentSerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = ['student', 'teacher', 'semester', 'instrument']


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    concert = ConcertSerializer(many=False, read_only=True)
    course = CourseSerializer(many=False, read_only=True)
    semester = SemesterSerializer(many=False, read_only=True)
    compositions = CompositionSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = ['concert', 'course', 'semester', 'compositions']


class RepetitionSerializer(serializers.HyperlinkedModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    composition = CompositionSerializer(many=False, read_only=True)

    class Meta:
        model = Repetition
        fields = ['course', 'composition', 'datetime', 'mark']
