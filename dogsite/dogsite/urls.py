from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dogsite import settings

urlpatterns = [
    path('', include('homepage.urls')),
    path('articles/', include('articles.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
