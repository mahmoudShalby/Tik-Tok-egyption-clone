from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video.urls')),
    path('auth/', include('users.urls')),
]
