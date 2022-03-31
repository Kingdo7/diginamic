from django.urls import path
from . import views
from .views import (
    C_Question,
    D_Question,
    U_Question,
    L_Question,
)

app_name = 'forum'


urlpatterns = [
    path("create/", views.Create, name = "Question"),
    #path("<slug:id>/update", views.Update, name="update"),
    path("detail/<int:id>/", views.Details, name="details"),
    path("", views.List, name='feed'),

]
