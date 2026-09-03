from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupLoginPage:

    # Define Locators as class attributes
    NEW_USER_SIGNUP_LOCATOR = (By.CSS_SELECTOR, '.signup-form h2')
    LOGIN_TO_ACCOUNT_LOCATOR = (By.CSS_SELECTOR, '.login-form h2')
    FULL_NAME_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    SIGNUP_EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    LOGIN_EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    LOGIN_PASSWORD_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
    SIGNUP_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
    LOGIN_INCORRECT_MESSAGE_LOCATOR = (By.XPATH , '//p[text()="Your email or password is incorrect!"]')
    EMAIL_ALREADY_EXISTS_LOCATOR = (By.XPATH , '//p[text()="Email Address already exist!"]')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to check that the 'New User Signup!' heading is visible
    def is_new_user_signup_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NEW_USER_SIGNUP_LOCATOR)
        )

    # Method to check that the 'New User Signup!' heading is visible
    def is_login_to_account_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_TO_ACCOUNT_LOCATOR)
        )

    # Method to enter the new user's full name at the initial signup
    def enter_signup_name(self, name):
        self.driver.find_element(*self.FULL_NAME_FIELD_LOCATOR).send_keys(name)

    # Method to enter a new user's email at initial signup
    def enter_signup_email(self, email):
        self.driver.find_element(*self.SIGNUP_EMAIL_FIELD_LOCATOR).send_keys(email)

    # Method to enter a returning user's email to log in
    def enter_login_email(self, email):
        self.driver.find_element(*self.LOGIN_EMAIL_FIELD_LOCATOR).send_keys(email)

    # Method to enter a returning user's password to log in
    def enter_login_password(self, password):
        self.driver.find_element(*self.LOGIN_PASSWORD_FIELD_LOCATOR).send_keys(password)

    # Combing methods for entering a returning user's credentials
    def enter_return_user_info(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)

    # Method to click the signup button
    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON_LOCATOR).click()

    # Combining methods to enter a new user's information for sign up
    def signup_new_user(self, name, email):
        self.enter_signup_name(name)
        self.enter_signup_email(email)

    # Method for clicking the login button
    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()

    def is_login_incorrect_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_INCORRECT_MESSAGE_LOCATOR)
        )

    def is_email_already_exists_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_ALREADY_EXISTS_LOCATOR)
        )