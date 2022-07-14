from django.conf import settings
from myapp import views
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('',views.main)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)