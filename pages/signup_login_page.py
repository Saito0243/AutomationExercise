from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupLoginPage:

    NEW_USER_SIGNUP_LOCATOR = (By.CSS_SELECTOR, '.signup-form h2')
    FULL_NAME_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    SIGNUP_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to check that the 'New User Signup!' heading is visible
    def is_new_user_signup_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NEW_USER_SIGNUP_LOCATOR)
        ).is_displayed()

    # Method to enter the user's full name at the initial signup
    def enter_signup_name(self, name):
        self.driver.find_element(*self.FULL_NAME_FIELD_LOCATOR).send_keys(name)

    # Method to enter the user's email at initial signup
    def enter_email_address(self, email):
        self.driver.find_element(*self.EMAIL_FIELD_LOCATOR).send_keys(email)

    # Method to click the signup button after entering the user's name and email
    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON_LOCATOR).click()

    # Combining methods into a clean workflow for the initial signup
    def signup_new_user(self, name, email):
        self.enter_signup_name(name)
        self.enter_email_address(email)
