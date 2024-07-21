from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('editor.urls')),  # Include the editor app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # 로그인 관련 URL
]
