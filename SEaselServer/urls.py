from django.contrib import admin
from django.urls import path, include
# from authorize.admin import school_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('school/admin/', school_admin_site.urls),
    path('auth/', include('authorize.urls')),
    path('api/', include('api.urls')),
]
