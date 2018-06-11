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

        add_question_button = self.browser.find_element_by_id('add_btn')

        heading2 = self.browser.find_element_by_tag_name('h2')
        self.assertIn('Question', heading2.text)
        # she see the question table
        question_table =  self.browser.find_element_by_id('question_table')

        # she want to add Question
        # She input the question text
        # she select the question answer
        # she click add button to create the question
        question_text.send_keys('1 + 1 = 2')
        ans_true.click()
        add_question_button.click()

        time.sleep(5)
        # she see the question in question_table

        question_text = self.browser.find_element_by_id('question')
        ans_true = self.browser.find_element_by_id('ans_t')
        ans_false = self.browser.find_element_by_id('ans_f')
        add_question_button = self.browser.find_element_by_id('add_btn')
        table = self.browser.find_element_by_id('question_table')
        rows = table.find_elements_by_tag_name('tr')
        rows_texts = [row.text for row in rows]

        self.assertTrue(
            any('1 + 1 = 2' in i for i in  rows_texts)
            )


        # she want to add another Question
        # She input the question text
        # she select the question answer
        # she click add button to create the question
        question_text = self.browser.find_element_by_id('question')
        ans_true = self.browser.find_element_by_id('ans_t')
        ans_false = self.browser.find_element_by_id('ans_f')
        question_text.send_keys('2 < 1')
        ans_false.click()
        add_question_button.click()

        time.sleep(5)
        # she see 2 questions in question_table
        question_text = self.browser.find_element_by_id('question')
        ans_true = self.browser.find_element_by_id('ans_t')
        ans_false = self.browser.find_element_by_id('ans_f')
        add_question_button = self.browser.find_element_by_id('add_btn')
        table = self.browser.find_element_by_id('question_table')
        rows = table.find_elements_by_tag_name('tr')
        rows_texts = [row.text for row in rows]

        self.assertTrue(
            any('1 + 1 = 2' in i for i in  rows_texts)
            )

        self.assertTrue(
            any('2 < 1' in i for i in  rows_texts)
            )




        self.fail('Finished the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
