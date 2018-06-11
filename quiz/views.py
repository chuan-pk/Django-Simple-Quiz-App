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

        return redirect('/')

    questions = Question.objects.all() 
    return render(request, 'quiz/home.html', {'question':questions})
