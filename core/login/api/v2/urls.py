from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginAPIView.as_view(), name='login'),
]
