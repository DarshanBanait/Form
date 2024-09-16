from django.urls import path
from . import views

urlpatterns = [
    path('', views.phq_gad_test_view, name='phq_gad_test'),
]
