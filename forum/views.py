from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Question_model
from .forms import CreateQuestion
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def Create(request):
    html_template = "forum/templates/Question.html"
    context = {}
    form = CreateQuestion(request.POST or None)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect("/")

    context['form'] = form
    return render(request, html_template, context)


def List(request):
    html_template = "forum/templates/Feed.html"
    context = {}
    context['dataset'] = Question_model.objects.all()

    return render(request, html_template, context)


def Details(request, id):
    html_template = "forum/templates/Detail.html"
    context = {}
    context['data'] = Question_model.objects.get(id = id)
    return render(request, html_template, context)


def Update(request, id):
    html_template = "forum/templates/Update.html"
    context = {}
    obj = get_object_or_404(Question_model, id = id )
    form = CreateQuestion(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context['form'] = form

    return render(request, html_template, context)
