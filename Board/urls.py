from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from advertisement.views import Register, EmailVerify
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('advertisement.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('register/confirm_email/', TemplateView.as_view(
        template_name='registration/confirm_email.html'), name='confirm_email'),
    path('register/confirm/', EmailVerify.as_view(), name='confirm'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)