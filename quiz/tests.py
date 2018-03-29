from django.test import TestCase
from django.urls import resolve
from quiz.views import home_page
from quiz.models import Question

# Create your tests here.
class HomePageTest(TestCase):

    def test_resolve_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_render_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'quiz/home.html')

class ModelsTest(TestCase):

    def test_can_save_question_to_database(self):
        first_question = Question()
        first_question.text = '1 + 1 = 2'
        first_question.ans = 'True'
        first_question.save()

        saved_items = Question.objects.all()
        self.assertEqual(saved_items.count(), 1)

        second_question = Question()
        second_question.text = '1 = 2'
        second_question.ans = 'False'
        second_question.save()

        saved_items = Question.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(Question.objects.all()[0].text, '1 + 1 = 2')
        self.assertEqual(Question.objects.all()[1].text, '1 = 2')
