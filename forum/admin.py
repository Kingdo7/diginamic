from django.contrib import admin

# Register your models here.
from .models import Question, Tag
class QuestionAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'date_creation']

class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_creation']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin )

