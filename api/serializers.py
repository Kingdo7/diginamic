from django.contrib.auth.models import User
from requests import Response
from rest_framework import serializers, status
from rest_framework.serializers import ModelSerializer

from forum.models import Question, Tag, Answer
from account.models import Profile
# QuestionVote, AnswerVote
# modelSerial Serialysers

from rest_framework.permissions import IsAuthenticated



class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class ProfileModelSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'point', 'bio', ]

        def create(self, validated_data):
            return Question.objects.create(**validated_data)


class QuestionModelSerializer(serializers.ModelSerializer):
    tag = TagModelSerializer()

    class Meta:
        model = Question
        fields = ['title', 'content', 'tag']
        extra_kwargs = {'tag': {'required': True}}

    def create(self, validated_data):
        tag = validated_data.pop('tag')
        try:
            tag = Tag.objects.get(title=tag['title'])
        except:
            tag = Tag.objects.create(title=tag['title'])
        return Question.objects.create(
            tag=tag, **validated_data  # will set other fields that were passed.
        )
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    def to_representation(self, obj):
        return {
            "tag": obj.tag.title
        }


class AnswerModelSerializer(ModelSerializer):
    question = serializers.CharField(source="question.title", read_only=True)
    date_creation = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)
    profile_answer = serializers.CharField(source="profile", read_only=True)

    class Meta:
        model = Answer
        fields = ['profile_answer', 'answer', 'date_creation', 'question']

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)


class AddVoteQuestionSerialiser(ModelSerializer):
    vote_questionlister = serializers.SerializerMethodField(source=Question)
    class Meta:
        model = Question
        fields = ['vote_questionlister']

    def get_votelister(self, obj):
        return obj.get_vote_list_count()

class AddVoteAnswerSerialiser(ModelSerializer):
    vote_answerslister = serializers.SerializerMethodField(source=Answer)

    class Meta:
        model = Answer
        fields = ['vote_answerslister']

    def get_votelister(self, obj):
        return obj.get_vote_list_count()


#ListVotesAnswerSerializer
class QuestionListVoteSerialiser(ModelSerializer):
    votelister = serializers.SerializerMethodField(source=Question)

    class Meta:
        model = Question
        fields = ['votelister']

    def get_votelister(self, obj):
        return obj.get_vote_list_count()

class AnswerListVoteSerialiser(ModelSerializer):
    votelister = serializers.SerializerMethodField(source=Answer)

    class Meta:
        model = Answer
        fields = ['votelister']

    def get_votelister(self, obj):
        return obj.get_vote_list_count()






# Vote









#class QuestionFunctionSerializer(serializers.Serializer):
#
#    title = serializers.CharField(max_length=150)
#    content = serializers.CharField(max_length=15000)
#    tag = serializers.ManyToManyField(Tag)
#
#    def create(self):
#        return Question.objects.create(validated_data)
#
#
#    def update(self, instance, validated_data):
#        instance.title = validated_data.get('title', instance.title)
#        instance.content = validated_data.get('content', instance.content)
#        #instance.tag = validated_data.get('tag', instance.tag)
#        instance.save()
#        return instance







#lass AnswerListSerializer(serializers.Serializer):

#   #question = serializers.ForeignKey(Question)
#   #profile = serializers.OneToOneField(eranswer)
#   answer = serializers.CharField(max_length=2000)

#   def create(self, validated_data):
#       return Question.objects.create(**validated_data)






#class QuestionListVotesSerializer(ModelSerializer):
#    class Meta:
#        model = QuestionVote
#        fields = ['profile','question', 'date_creation']

#class AnswerListVotesSerializer(ModelSerializer):
#    class Meta:
#        model = AnswerVote
#        fields = ['answer','profile', 'date_creation']





#class QuestionCreateVoteSerializer(ModelSerializer):
 #   class Meta:
#        model = QuestionVote
#        fields = ['question']


#class QuestionListSerializer(serializers.Serializer):
   # title = serializers.CharField(max_length=150)
    #content = serializers.CharField(max_length=15000)
    #tag = serializers.ManyToManyField(Tag)

    #def create(self):
    #    return Question.objects.create(validated_data)
#
    #def update(self, instance, validated_data):
    #    instance.titre = validated_data.get('titre', instance.titre)
    #    instance.sous_titre = validated_data.get('sous_titre', instance.sous_titre)
    #    instance.contenu = validated_data.get('contenu', instance.contenu)
    #    instance.save()
    #    return instance

