import jsonpickle
from django.db.models import Avg
from django.http import HttpResponseNotFound
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from api.serializers import *
from utils.recommendations import get_recommendations


class MusicSchoolViewSet(viewsets.ModelViewSet):
    queryset = MusicSchool.objects.all().order_by('name')
    serializer_class = MusicSchoolSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('name')
    serializer_class = TeacherSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all().order_by('name')
    serializer_class = AdministratorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all().order_by('number')
    serializer_class = SemesterSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class CompositionRepresentationViewSet(viewsets.ModelViewSet):
    queryset = CompositionRepresentation.objects.all()
    serializer_class = CompositionRepresentationSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class RepetitionViewSet(viewsets.ModelViewSet):
    queryset = Repetition.objects.all()
    serializer_class = RepetitionSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


class MusicListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        music = CompositionRepresentation.objects.filter(
            composition__program__course__student_id__exact=request.user.id).all()
        content = [dict(composition_representation_id=m.id,
                        composition_id=m.composition_id,
                        name=m.composition.name,
                        instrument=m.composition.instrument.name,
                        author=m.composition.author,
                        difficulty=m.composition.difficulty,
                        format=m.format) for m in music]
        return Response(content)


class MusicRepresentationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, composition_representation_id=None):
        if not composition_representation_id:
            return HttpResponseNotFound()
        music = CompositionRepresentation.objects.filter(id=composition_representation_id).first()
        content = music.sheme
        return Response(content)


class MusicRecommendationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = {}
        request_data = request.data
        if not ("concert_id" in request_data and "student_id" in request_data):
            return HttpResponseNotFound()
        course = Course.objects.filter(student_id=request_data['student_id']).first()
        program = Program(concert_id=request_data['concert_id'], course=course, semester=course.semester)
        program.save()
        music = get_recommendations(program)
        program.compositions.set(music)
        program.save()
        return Response()


class StudentListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        courses = Course.objects.filter(teacher_id=request.user.id)
        content = [dict(studentId=c.student.id,
                        name=c.student.name,
                        semester=c.semester.number,
                        instrument=c.instrument.name) for c in courses]
        return Response(content)


def get_avg_mark(course_id, composition_id):
    return Repetition.objects.filter(course_id=course_id, composition_id=composition_id).aggregate(Avg('mark'))[
        'mark__avg']


class StudentInfoView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, student_id=None):
        student = Student.objects.filter(id=student_id).get()
        programs = list(Program.objects.filter(course__student_id=student_id))
        concerts = []
        for program in programs:
            concerts.append(dict(
                date=str(program.concert.date),
                compositions=[
                    dict(
                        compositionId=composition.id,
                        name=composition.name,
                        author=composition.author,
                        difficulty=composition.difficulty,
                        averageMark=get_avg_mark(program.course_id, composition.id)
                    )
                    for composition in list(program.compositions.get_queryset())
                ]
            ))

            content = dict(name=student.name,
                           concerts=concerts)
            return Response(content)


class PossibleConcertsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, student_id=None):
        programs = list(Program.objects.filter(course__student_id=student_id))
        concerts = list(Concert.objects.exclude(program__in=programs))
        content = [
            dict(
                concertId=concert.id,
                date=concert.date
            )
            for concert in concerts]
        return Response(content)


class StudentRepetitionsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, student_id=None, composition_id=None):
        repetitions = Repetition.objects.filter(course__student_id=student_id, composition_id=composition_id)
        content = [
            dict(
                dateTime=repetition.datetime,
                mark=repetition.mark,
                instrument=repetition.course.instrument.name,
            )
            for repetition in repetitions
        ]
        return Response(content)
