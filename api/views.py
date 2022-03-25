from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import QuestionListSerializer, QuestionModelSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from forum.models import Question
from rest_framework_simplejwt.authentication import JWTAuthentication

class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

    def get_serializer_context(self, **kwargs):
        context = super().get_serializer_context(**kwargs)
        print(context)
        return context

class QuestionCreateAPI(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer

class QuestionUpdateAPI(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer


