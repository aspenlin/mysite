from django.contrib import admin
from .models import Question, Choice
from tinymce.widgets import TinyMCE
from django.db import models

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Description', {'fields':['description']}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
