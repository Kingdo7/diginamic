from django.forms import ModelForm
from .models import Create_Question

class CreateQuestion(ModelForm):
    class Meta :
        model = Create_Question
        fields = ['title', 'question']