from django.urls import path, include
from rest_framework import routers

from .views import (
    MusicListView,
    MusicRepresentationView,
    MusicRecommendationView,
    MusicSchoolViewSet,
    UserViewSet,
    CompositionViewSet,
    ConcertViewSet,
    CourseViewSet,
    InstrumentViewSet,
    ProgramViewSet,
    RepetitionViewSet,
    SemesterViewSet,
    CompositionRepresentationViewSet,
    StudentListView,
    StudentInfoView,
    PossibleConcertsView,
    StudentRepetitionsView,
    StudentViewSet,
    AdminViewSet,
    TeacherViewSet,
    FeedbackViewSet)

router = routers.DefaultRouter()
router.register(r'schools', MusicSchoolViewSet)
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'concerts', ConcertViewSet)
router.register(r'compositions', CompositionViewSet)
router.register(r'composition_representations', CompositionRepresentationViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'repetitions', RepetitionViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('music/', MusicListView.as_view()),
    path('music/<int:composition_representation_id>/', MusicRepresentationView.as_view()),
    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
    path('teacher/students/', StudentListView.as_view()),
    path('student/<int:student_id>/', StudentInfoView.as_view()),
    path('student/<int:student_id>/concerts/', PossibleConcertsView.as_view()),
    path('student/<int:student_id>/recommend/', MusicRecommendationView.as_view()),
    path('student/<int:student_id>/<int:composition_id>/', StudentRepetitionsView.as_view()),
]
