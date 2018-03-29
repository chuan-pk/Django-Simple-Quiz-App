from django.shortcuts import render
from quiz.models import Question

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        q = Question()

        question_text = request.POST.get('question_text','')
        ans = request.POST.get('ans','')

        q.text = question_text
        q.ans = ans
        q.save()

        return render(request, 'quiz/home.html', {'question':question_text})


    return render(request, 'quiz/home.html', {'question':'-'})
