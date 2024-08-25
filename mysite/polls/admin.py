from django.contrib import admin
from .models import Question

#admin.site.register(Question)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	fields = ["question_text"]

