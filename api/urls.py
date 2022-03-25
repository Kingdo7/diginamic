from django.urls import path
from rest_framework import routers

from .views import (
    QuestionList,
    QuestionCreateAPI,
    QuestionUpdateAPI,

)

from rest_framework import routers
router = routers.DefaultRouter()


app_name = 'api'


urlpatterns = [
    path('questions/', QuestionList.as_view(), name="article-list"),
    path('questions/create/', QuestionCreateAPI.as_view(), name="article-create"),
    path('questions/<int:pk>/update', QuestionUpdateAPI.as_view(), name="article-update"),

]