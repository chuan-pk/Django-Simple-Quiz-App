from selenium import webdriver
from django.test import LiveServerTestCase
import time

class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()

    def test_01_can_create_question(self):

        # Editch check out the Quiz app homepage
        self.browser.get(self.live_server_url)
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

        time.sleep(1)
        # she see the question in question_table
        question_text = self.browser.find_element_by_id('question')
        ans_true = self.browser.find_element_by_id('ans_t')
        ans_false = self.browser.find_element_by_id('ans_f')
        add_question_button = self.browser.find_element_by_id('add_btn')
        table = self.browser.find_element_by_id('question_table')
        rows = table.find_elements_by_tag_name('tr')
        rows_texts = [row.text for row in rows]
        self.assertTrue(
            any(all(a in i for a in ['1 + 1 = 2', 'correct answer: 0', 'total answer: 0']) for i in rows_texts)
            )


        # she see the radio button and submit button of first question
        ans_true1 = self.browser.find_element_by_id('ans_t_1')
        ans_false1 = self.browser.find_element_by_id('ans_f_1')
        submit1 = self.browser.find_element_by_id('submit_btn_1')


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

        time.sleep(1)
        # she see 2 questions in question_table
        question_text = self.browser.find_element_by_id('question')
        ans_true = self.browser.find_element_by_id('ans_t')
        ans_false = self.browser.find_element_by_id('ans_f')
        add_question_button = self.browser.find_element_by_id('add_btn')
        table = self.browser.find_element_by_id('question_table')
        rows = table.find_elements_by_tag_name('tr')
        rows_texts = [row.text for row in rows]

        # No one Ans question so Answer count = 0 and correct count = 0
        self.assertTrue(
            any(all(a in i for a in ['1 + 1 = 2', 'correct answer: 0', 'total answer: 0']) for i in rows_texts)
            )

        # she see the radio button and submit button of first question
        ans_true1 = self.browser.find_element_by_id('ans_t_1')
        ans_false1 = self.browser.find_element_by_id('ans_f_1')
        submit1 = self.browser.find_element_by_id('submit_btn_1')

        self.assertTrue(
            any(all(a in i for a in ['2 < 1', 'correct answer: 0', 'total answer: 0']) for i in rows_texts) 
            )

        # she see the radio button and submit button of second question
        ans_true1 = self.browser.find_element_by_id('ans_t_2')
        ans_false1 = self.browser.find_element_by_id('ans_f_2')
        submit1 = self.browser.find_element_by_id('submit_btn_2')

        # She left this website
        self.browser.quit()


        ## The database torn down every test method 
        ## So i move second method to this method

        # John go to website
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        self.assertIn('Quiz', self.browser.title)

        time.sleep(1)
        # He see 2 questions in question_table
        question_text = self.browser.find_element_by_id('question')
        ans_true = self.browser.find_element_by_id('ans_t')
        ans_false = self.browser.find_element_by_id('ans_f')
        add_question_button = self.browser.find_element_by_id('add_btn')
        table = self.browser.find_element_by_id('question_table')
        rows = table.find_elements_by_tag_name('tr')
        rows_texts = [row.text for row in rows]

        self.assertTrue(
            any(all(a in i for a in ['1 + 1 = 2', 'correct answer: 0', 'total answer: 0']) for i in rows_texts)
            )

        self.assertTrue(
            any(all(a in i for a in ['2 < 1', 'correct answer: 0', 'total answer: 0']) for i in rows_texts) 
            )

        # He see the radio button and submit button of first question
        ans_true1 = self.browser.find_element_by_id('ans_t_1')
        ans_false1 = self.browser.find_element_by_id('ans_f_1')
        submit1 = self.browser.find_element_by_id('submit_btn_1')

        # He see the radio button and submit button of second question
        ans_true2 = self.browser.find_element_by_id('ans_t_2')
        ans_false2 = self.browser.find_element_by_id('ans_f_2')
        submit2 = self.browser.find_element_by_id('submit_btn_2')

        # He want to answer first question
        ans_true1.click()
        submit1.click()

        question_text = self.browser.find_element_by_id('question')
        ans_true = self.browser.find_element_by_id('ans_t')
        ans_false = self.browser.find_element_by_id('ans_f')
        add_question_button = self.browser.find_element_by_id('add_btn')
        table = self.browser.find_element_by_id('question_table')
        rows = table.find_elements_by_tag_name('tr')
        rows_texts = [row.text for row in rows]


        self.assertTrue(
            any(all(a in i for a in ['1 + 1 = 2', 'correct answer: 1', 'total answer: 1']) for i in rows_texts)
            )

        self.assertTrue(
            any(all(a in i for a in ['2 < 1', 'correct answer: 0', 'total answer: 0']) for i in rows_texts) 
            )

        self.fail('Finished the test!')


      
if __name__ == '__main__':
    unittest.main(warnings='ignore')     # luanches the unittest test runner