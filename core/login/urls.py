from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import TemplateView

app_name = "login"

urlpatterns = [
    path("", TemplateView.as_view(), name="index"),
    path("api/v1/", include("login.api.v1.urls")),
    path("api/v2/", include("login.api.v2.urls")),
]
