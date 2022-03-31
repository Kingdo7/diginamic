from django.forms import ModelForm
from .models import Question_model

class CreateQuestion(ModelForm):
    class Meta :
        model = Question_model
        fields = ['title', 'question']

class Details(ModelForm):
    class Meta :
        model = Question_model
        fields = ['answer']
