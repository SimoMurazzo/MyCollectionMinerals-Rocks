from django.urls import path
from Minerals.views import *

urlpatterns = [
    path('detail/<int:pk>/', MineralDetail.as_view(), name='detail'),
]
