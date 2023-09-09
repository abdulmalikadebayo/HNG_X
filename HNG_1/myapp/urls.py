from django.urls import path
from .views import GetInfoView

urlpatterns = [
    path('get_info/', GetInfoView.as_view(), name='get_info'),
]
