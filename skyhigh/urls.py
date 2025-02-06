
#C:\Users\Admin\Desktop\skyhigh\skyhigh\urls.py
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from ckeditor_uploader import urls as ckeditor_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('ckeditor/', include(ckeditor_urls)),  # Add CKEditor uploader URLs
    
    path('brand/', include('brand.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
