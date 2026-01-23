from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: {'message': 'Jobs API working!'}, name='job-list'),
]
