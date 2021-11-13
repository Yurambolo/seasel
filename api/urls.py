from django.urls import path, include
from rest_framework import routers

from .views import (
    MusicListView,
    MusicRepresentationView,
    MusicRecommendationView,
    MusicSchoolViewSet,
    StudentViewSet,
    AdministratorViewSet,
    CompositionViewSet,
    ConcertViewSet,
    CourseViewSet,
    InstrumentViewSet,
    ProgramViewSet,
    RepetitionViewSet,
    SemesterViewSet,
    TeacherViewSet,
    CompositionRepresentationViewSet)

router = routers.DefaultRouter()
router.register(r'schools', MusicSchoolViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'administrators', AdministratorViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'concerts', ConcertViewSet)
router.register(r'compositions', CompositionViewSet)
router.register(r'composition_representations', CompositionRepresentationViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'repetitions', RepetitionViewSet)

urlpatterns = [
    path('music/', MusicListView.as_view()),
    path('music/<int:composition_representation_id>/', MusicRepresentationView.as_view()),
    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
    path('recommend/<int:program_id>/', MusicRecommendationView.as_view()),
]
