from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
from .models import Question, Answer

# admin.site.register(Question)
# admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)