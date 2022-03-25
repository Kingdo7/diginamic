from django.urls import path
from . import views

from .views import (

    UserCreateView,
    UserLoginView,
    UserLogoutView,
    Index,
    ProfileUpdateView,
    ProfileListView,
    ProfileDetailsView,

)


app_name = 'account'

urlpatterns = [

    path('auth/profile/<int:pk>/update/', ProfileUpdateView.as_view(), name = "profile-update"),
    path('auth/profile/<int:pk>/details/', ProfileDetailsView.as_view(), name = "profile-details"),
    path('auth/profile/list/', ProfileListView.as_view(), name = "profile-list"),
    path('auth/register/', UserCreateView.as_view(), name = "register"),
    path('auth/login/', UserLoginView.as_view(), name="signup"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('', Index.as_view(), name="index"),
    # path("landing/", views.landing, name="landing"),
    # path("profile/", views.profile, name="profile"),
    # path("Create_question/", views.createquestion, name="create_question"),
    # path("SocialNetwork/", views.sociale, name="Network"),
]

