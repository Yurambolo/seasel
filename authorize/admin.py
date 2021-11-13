from django.contrib import admin
from api.models import *
from authorize.models import Administrator

admin.site.register(MusicSchool)
admin.site.register(Administrator)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Instrument)
admin.site.register(Course)
admin.site.register(Concert)
admin.site.register(CompositionRepresentation)
admin.site.register(Composition)
admin.site.register(Repetition)
admin.site.register(Program)


# from authorize.models import Administrator, Student
# from .forms import AdminRegisterForm
#
#
# class SchoolAdminSite(admin.AdminSite):
#     site_header = "School Administration"
#
#
# school_admin_site = SchoolAdminSite(name='school_admin')
#
#
# @admin.register(Administrator)
# class AdministratorAdmin(admin.ModelAdmin):
#     form = AdminRegisterForm
#
#     def get_queryset(self, request):
#         qs = super(AdministratorAdmin, self).get_queryset(request)
#         music_school = request.user.music_school
#         return qs.filter(music_school=music_school)
