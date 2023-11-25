from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("sage", views.predict_using_sagemaker_local_mode, name="sagemaker")
]
