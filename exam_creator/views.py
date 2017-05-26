from django.shortcuts import render

# Create your views here.

def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})


