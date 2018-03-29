from django.shortcuts import render

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text','')
        return render(request, 'quiz/home.html', {'question':question_text})


    return render(request, 'quiz/home.html', {'question':'-'})
