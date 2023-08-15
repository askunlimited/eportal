from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # Folder Url Path
    path("folder/", include("folder.urls")),
    path("document/", include("document.urls")),
    # Userprofiles, departments and account url path
    path("", include("userprofiles.urls")),
    # path("log-out/", views.LogoutView.as_view(), name="log-out"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
