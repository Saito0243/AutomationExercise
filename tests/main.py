import data
from selenium import webdriver
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.registration_detail_page import RegistrationDetailPage

class TestAutomationExercise:
    @classmethod
    def setup_class(cls):
        # 1. Launch browser
        cls.driver = webdriver.Chrome()

    def test_register_user(self):
        # 2. Navigate to url
        self.driver.get("https://automationexercise.com/")
        home_page = HomePage(self.driver)
        signup_login_page = SignupLoginPage(self.driver)
        registration_detail_page = RegistrationDetailPage(self.driver)

        # 3. Verify that home page is visible successfully
        assert home_page.is_page_visible()

        # 4. Click on 'Signup / Login' button
        home_page.click_signup_login_link()

        # 5. Verify 'New User Signup!' is visible
        assert signup_login_page.is_new_user_signup_visible()

        # 6. Enter name and email address
        # 7. Click 'Signup' button
        signup_login_page.signup_new_user(data.FULL_NAME, data.EMAIL)

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        assert registration_detail_page.enter_acct_info_visible()

        # 9. Fill details: Title, Name, Email, Password, Date of birth
        registration_detail_page.select_user_title()
        registration_detail_page.enter_new_user_password(data.PASSWORD)
        registration_detail_page.enter_new_user_full_birthdate(data.BIRTH_DAY, data.BIRTH_MONTH, data.BIRTH_YEAR)

        # 10. Select checkbox 'Sign up for our newsletter!'
        # 11. Select checkbox 'Receive special offers from our partners!'
        registration_detail_page.select_optional_opt_ins()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
