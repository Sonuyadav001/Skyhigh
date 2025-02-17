
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('brand/', include('brand.urls')),
]

# Serve media files in development only
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

