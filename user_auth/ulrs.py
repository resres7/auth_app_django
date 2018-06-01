from django.contrib import admin, auth
from django.urls import path, include

from something.views import something

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authapp.urls")),
    path("", include("user_auth.ulrs")),
    path("accounts", include("django.contrib.auth.urls")),
]