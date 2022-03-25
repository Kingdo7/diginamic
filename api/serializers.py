from django.contrib.auth.models import User
from requests import Response
from rest_framework import serializers, status
from rest_framework.serializers import ModelSerializer

from forum.models import Question, Tag

# modelSerial Serialysers

from rest_framework.permissions import IsAuthenticated


class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'content']

class QuestionListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField(max_length=250)
    #tag = serializers.ManyToManyField(Tag)

    def create(self):
        print()
        return Question.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.titre = validated_data.get('titre', instance.titre)
        instance.sous_titre = validated_data.get('sous_titre', instance.sous_titre)
        instance.contenu = validated_data.get('contenu', instance.contenu)
        instance.save()
        return instance

