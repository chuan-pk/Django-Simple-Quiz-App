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

        # She see the input box to create question


if __name__ == '__main__':
    unittest.main(warnings='ignore')
