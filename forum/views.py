from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Question_model
from .forms import CreateQuestion, Details
from django.views.generic import CreateView, ListView, UpdateView, DetailView
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
    context['data'] = Question_model.objects.get(id=id)
    form = Details(request.POST or None)
    context['form'] = form
    return render(request, html_template, context)


def Update(request, id):
    html_template = "forum/templates/Update.html"
    context = {}
    obj = get_object_or_404(Question_model, id = id)
    form = CreateQuestion(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context['form'] = form

    return render(request, html_template, context)

class C_Question(CreateView):
    model = Question_model
    html_template = "forum/templates/Question.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = CreateQuestion()
        return render(request, self.html_template, context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = CreateQuestion(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        context['form'] = form
        return render(request, self.html_template, context)

class D_Question(DetailView):
    model = Question_model
    html_template = "forum/templates/Detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Question_model.objects.get(id=id)
        return context


class L_Question(ListView):
    model = Question_model
    html_template = "forum/templates/Feed.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['dataset'] = Question_model.objects.all()
        return render(request, self.html_template, context)

class U_Question(UpdateView) :
    model = Question_model
    html_template = "forum/templates/Update.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = Update()
        return render(request, self.html_template, context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = Update(request.POST or None, id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context['form'] = form
        return render(request, self.html_template, context)

