import jsonpickle
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
                        dificulty=m.composition.difficulty,
                        format=m.format) for m in music]
        return Response(jsonpickle.encode(content, unpicklable=False))


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

    def get(self, request, format=None, program_id=None):
        program = Program.objects.filter(id=program_id).first()
        if not program:
            return HttpResponseNotFound()
        music = get_recommendations(program)
        program.compositions.set(music)
        program.save()
        content = jsonpickle.encode(music, unpicklable=False)
        return Response(content)
