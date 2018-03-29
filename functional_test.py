from selenium import webdriver
import unittest
import time

class HomePageTest(unittest.TestCase):
    """
        Test HomePage
        home page = create question page
        home page have link to ans question
    """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()

    def test_can_create_question(self):

        # Editch check out the Quiz app homepage
        self.browser.get('http://localhost:8000')
        # She see the browser title
        self.assertIn('Quiz', self.browser.title)

        # she see the web heading
        heading1 = self.browser.find_element_by_tag_name('h1')
        self.assertIn('create question', heading1.text)

        # She see the input box to create question
        # two radio button to select answer
        # and create button
        question_text = self.browser.find_element_by_id('question')
        self.assertEqual(question_text.get_attribute('placeholder'), 'Enter Question')

        ans_true = self.browser.find_element_by_id('ans_t')
        self.assertEqual(ans_true.get_attribute('value'), 'True')

        ans_false = self.browser.find_element_by_id('ans_f')
        self.assertEqual(ans_false.get_attribute('value'), 'False')



        self.fail('Finished the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
