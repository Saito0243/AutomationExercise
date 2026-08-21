from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data


class AutoExercisePage:

    # Define Locators as class attributes
    LOGO_LOCATOR = (By.XPATH,'//img[@src="/static/images/home/logo.png"]')
    SIGNUP_LOGIN_LINK_LOCATOR = (By.XPATH, '//a[@href="/login"]')
    NEW_USER_SIGNUP_LOCATOR = (By.XPATH, '//h2[text()="New User Signup!"]')
    FULL_NAME_FIELD_LOCATOR = (By.XPATH, '//input[@data-qa="signup-name"]')
    EMAIL_FIELD_LOCATOR = (By.XPATH, '//input[@data-qa="signup-email"]')
    SIGNUP_BUTTON_LOCATOR = (By.XPATH, '//button[@data-qa="signup-button"]')
    ENTER_ACCT_INFO_LOCATOR = (By.XPATH, '//b[text()="Enter Account Information"]')
    TITLE_MR_RADIO_LOCATOR = (By.XPATH, '//input[@value="Mr"]')
    SIGNUP_PASSWORD_LOCATOR = (By.XPATH, '//input[@type="password"]')
    BIRTH_DAY_DROPDOWN_LOCATOR = (By.XPATH, '//select[@id="days"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to use page's logo to check if the home page is visible
    def is_page_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGO_LOCATOR)
        ).is_displayed()

    # Method to click the 'Signup/Login' link at the top of the home page
    def click_signup_login_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN_LINK_LOCATOR)
        ).click()

    # Method to check that the 'New User Signup!' heading is visible
    def is_new_user_signup_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NEW_USER_SIGNUP_LOCATOR)
        ).is_displayed()

    # Method to enter the user's full name at the initial signup
    def enter_signup_name(self):
        self.driver.find_element(*self.FULL_NAME_FIELD_LOCATOR).send_keys(data.FULL_NAME)

    # Method to enter the user's email at initial signup
    def enter_email_address(self):
        self.driver.find_element(*self.EMAIL_FIELD_LOCATOR).send_keys(data.EMAIL)

    # Method to click the signup button after entering the user's name and email
    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON_LOCATOR).click()

    # Combining methods into a clean workflow for the initial signup
    def signup_new_user(self):
        self.enter_signup_name()
        self.enter_email_address()
        self.click_signup_button()

    # Method to verify that 'ENTER ACCOUNT INFORMATION' is visible
    def enter_acct_info_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ENTER_ACCT_INFO_LOCATOR)
        ).is_displayed()

    # Method to select Mr as the user's title
    def select_user_title(self):
        self.driver.find_element(*self.TITLE_MR_RADIO_LOCATOR).click()

    # Method to enter a password for the new user
    def enter_new_user_password(self):
        self.driver.find_element(*self.SIGNUP_PASSWORD_LOCATOR).send_keys(data.PASSWORD)

    # Method to enter the new users DOB
    def enter_date_of_birth(self):
