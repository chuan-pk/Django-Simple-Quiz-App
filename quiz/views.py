from django.shortcuts import render, redirect
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
    return render(request, 'quiz/home.html', {'questions':questions})

def ans_quiz(request, question_id):
    if request.method == 'POST':
        print(question_id)
        q = Question.objects.get(id=question_id)           # get question from DB
        ans = request.POST.get('ans', '')               # get ans from POST request
        q.count += 1                                    # increase ans people
        
        # if ans is correct the increase correct people count
        if ans == q.ans:
            q.correct_count += 1 

        q.save()

        return redirect('/')