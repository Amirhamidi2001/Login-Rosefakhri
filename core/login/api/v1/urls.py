from django.urls import path
from .views import *

app_name = "api_v1"

urlpatterns = [
    path('', LoginAPIView.as_view(), name='login'),
]
