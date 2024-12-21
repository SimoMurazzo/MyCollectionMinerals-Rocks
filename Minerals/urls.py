from django.urls import path


urlpatterns = [
    path('list/', View.as_view(), name='list')
]
