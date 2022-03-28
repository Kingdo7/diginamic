from django.http import HttpResponse
from django.shortcuts import render
from .models import Create_Question
from .forms import CreateQuestion
from django.views.generic import CreateView, View, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

## Voir comment améliorer l'affichage du titre et de la question
## Ajouter le Tag
def Create_question(request):
    html_template = 'forum/templates/Question.html'

    if request.method == "POST" :
        form = CreateQuestion(request.POST)
    else :
        form = CreateQuestion()

    context = {'form':form}
    return render(request, html_template, context)

class Create_Question(CreateView):
    html_template = 'forum/templates/Question.html'
    success_url = reverse_lazy('forum:feed')

    def get(self,request):
        context = {}
        context['form'] = CreateQuestion
        return render(request, self.html_template, context)

    def POST(self, request, **kwargs):
        context = {}
        context['form'] = CreateQuestion
        title = request.POST['title']
        question = request.POST['question']

        if title == '':
            messages.error(request, "Vous n'avez pas renseigné de titre")
        elif question == '':
            messages.error(request, "Vous n'avez pas renseigné votre quesiton")

        return render(request, self.html_template, context)


class feed(ListView):
    html_template = 'forum/templates/Feed.html'
    model = CreateQuestion
    paginate_by = 8
    context_object_name = "Questions"

class Detail_View(DetailView):
    html_template = "forum/templates/Detail.html"
    slug_field = 'id'
    slug_url_kwarg = 'question_id'
    queryset = CreateQuestion.objects.all()
    context_object_name = 'question'