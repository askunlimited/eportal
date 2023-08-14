from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("userprofiles.urls")),
    path("log-out/", views.LogoutView.as_view(), name="log-out"),
    path(
        "",
        views.LoginView.as_view(template_name="userprofiles/log-in.html"),
        name="log-in",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
