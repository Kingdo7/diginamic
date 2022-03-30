from django.urls import path
from . import views


app_name = 'forum'


urlpatterns = [
    path("create/", views.Create, name = "Question"),
    path("<str:id>/update", views.Update, name="update"),
    path("details/<str:id>", views.Details, name="details"),
    path("", views.List, name='feed'),
]
