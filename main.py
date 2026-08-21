import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages import AutoExercisePage

class TestAutomationExercise:
    @classmethod
    def setup_class(cls):
        # 1. Launch browser
        cls.driver = webdriver.Chrome()

    def test_register_user(self):
        # 2. Navigate to url 'http://automationexercise.com'
        self.driver.get("http://automationexercise.com/")
        auto_exercise_page = AutoExercisePage(self.driver)

        # 3. Verify that home page is visible successfully
        assert auto_exercise_page.is_page_visible()

        # 4. Click on 'Signup / Login' button
        auto_exercise_page.click_signup_login_link()

        # 5. Verify 'New User Signup!' is visible
        assert auto_exercise_page.is_new_user_signup_visible()

        # Entering the name and email, and clicking the signup button
        auto_exercise_page.signup_new_user()

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        assert auto_exercise_page.enter_acct_info_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
