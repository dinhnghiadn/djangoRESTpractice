from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from apps.user.views import UserRegisterView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    path('subject/', include('apps.subject.urls')),
    path('student/', include('apps.student.urls')),
    path('teacher/', include('apps.teacher.urls')),
    path('class/', include('apps.classes.urls')),
    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
