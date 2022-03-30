from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status


from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import  TagModelSerializer, QuestionModelSerializer, AnswerModelSerializer, AddVoteQuestionSerialiser, AddVoteAnswerSerialiser, QuestionListVoteSerialiser, AnswerListVoteSerialiser, ProfileModelSerializer
from rest_framework.views import APIView
from forum.models import Question, Answer, Tag
from account.models import  Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.generic import TemplateView


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer













#models.view et créer des truc dedans
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)




class QuestionListAPI(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer

# Enelver le null dans models pour question. Ca va faire un problme not nullc onstraint mais c'ets normal car il faut récupérer via token, l'id de user et faire l'ajout quand une quesiton est crée.
class QuestionCreateAPI(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.objects.all())

# A Faire et modifier pour la prochaine fois
class QuestionDetailAPI(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer

class QuestionUpdateAPI(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer



#Answer
class QuestionAnswersListAPI(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = AnswerModelSerializer

    def get_queryset(self):
        return Answer.objects.filter(question__id=self.kwargs['pk'])



# A Faire et modifier pour la prochaine fois pour associéer au profil directement
# COCmme pas d enull dans models, probleme not nul contrain => associer automatiquement le profil connecvté.
class AnswerCreateAPI(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.objects.all())


class AnswerDetailAPI(RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer

#Vote à améliorer  en fonction de l'utilisateur qui se connecte et utilise le token



class AddVoteQuestionAPI(UpdateAPIView):

    queryset = Question.objects.all()
    serializer_class = AddVoteQuestionSerialiser
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        qs = self.get_object()
        if self.request.user in qs.votelist.all():
            qs.votelist.remove(self.request.user)
        else:
            qs.votelist.add(self.request.user)
        serializer.save()


class AddVoteAnswerAPI(UpdateAPIView):

    queryset = Answer.objects.all()
    serializer_class = AddVoteAnswerSerialiser
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        qs = self.get_object()
        if self.request.user in qs.votelist.all():
            qs.votelist.remove(self.request.user)
        else:
            qs.votelist.add(self.request.user)
        serializer.save()



# Vote
class QuestionListVoteAPI(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListVoteSerialiser
    #def get_queryset(self):
    #    return Question.objects.filter(question__id=self.kwargs['pk'])

class AnswerListVoteAPI(RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListVoteSerialiser



#Profile

class ProfileListAPI(ListAPIView):
    queryset = Profile.objects.all().order_by('first_name')
    serializer_class = ProfileModelSerializer

class ProfileDetailAPI(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer

class ProfileUpdateAPI(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer