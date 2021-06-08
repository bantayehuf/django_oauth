from django.urls import path

from .views import sample_views

urlpatterns = [
    path('',sample_views.wecome, name='welcome'),
]
