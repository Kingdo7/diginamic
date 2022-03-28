from django.urls import path
from . import views


app_name = 'forum'


urlpatterns = [
    path("Create_Question/", views.Create_question, name = "Question"),
    path("", views.ListView.as_view(), name='feed')
]