from django.urls import path
from .views import task1

urlpatterns = [
    path('api/', task1.as_view(), name='api'),
]