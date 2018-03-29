from django.test import TestCase
from django.urls import resolve
from quiz.views import home_page


# Create your tests here.
class HomePageTest(TestCase):

    def test_resolve_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_render_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'quiz/home.html')
