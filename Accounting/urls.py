from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('session/', include('session.urls')),
    path('fee/', include('fee.urls')),
    path('student/', include('student.urls')),
    path('class/', include('student_class.urls')),
    path('session/', include('session.urls')),
    path('staff/', include('staff.urls')),
    path('finance/', include('finance.urls')),

]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)