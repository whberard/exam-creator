from django.shortcuts import render
from .models import Question, Topic

# Create your views here.

def questions_list(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})


