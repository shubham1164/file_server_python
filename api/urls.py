from django.urls import include, path
from . import views

urlpatterns = [
  path('upload/eeg', views.upload_eeg),
  path('upload/ppg', views.upload_ppg),
  path('output', views.read_output)
]