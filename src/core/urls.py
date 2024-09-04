from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexViwew.as_view(), name="index"),
]
