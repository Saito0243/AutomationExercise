from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutoExercisePage:

    # Define Locators as class attributes
    # LOGO_LOCATOR = (By.CSS_SELECTOR,".logo img")
    # SIGNUP_LOGIN_LINK_LOCATOR = (By.LINK_TEXT, 'Signup / Login')
    NEW_USER_SIGNUP_LOCATOR = (By.CSS_SELECTOR, '.signup-form h2')
    FULL_NAME_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    SIGNUP_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
    ENTER_ACCT_INFO_LOCATOR = (By.CSS_SELECTOR, '#form .login-form h2 b')
    TITLE_MR_RADIO_LOCATOR = (By.ID, 'id_gender1')
    SIGNUP_PASSWORD_LOCATOR = (By.ID, 'password')
    BIRTH_DAY_DROPDOWN_LOCATOR = (By.ID, 'days')
    BIRTH_MONTH_DROPDOWN_LOCATOR = (By.ID, 'months')
    BIRTH_YEAR_DROPDOWN_LOCATOR = (By.ID, 'years')
    NEWSLETTER_CHECKBOX_LOCATOR = (By.ID, 'newsletter')
    OPT_IN_CHECKBOX_LOCATOR = (By.ID, 'optin')
    FIRST_NAME_INPUT_LOCATOR = (By.ID, 'first_name')
    LAST_NAME_INPUT_LOCATOR = (By.ID, 'last_name')
    COMPANY_INPUT_LOCATOR = (By.ID, 'company')
    ADDRESS_1_INPUT_LOCATOR = (By.ID, 'address1')
    ADDRESS_2_INPUT_LOCATOR = (By.ID, 'address2')
    COUNTRY_DROPDOWN_LOCATOR = (By.ID, 'country')
    STATE_INPUT_LOCATOR = (By.ID, 'state')
    CITY_INPUT_LOCATOR = (By.ID, 'city')
    ZIP_CODE_INPUT_LOCATOR = (By.ID, 'zipcode')
    MOBILE_NUMBER_INPUT_LOCATOR = (By.ID, 'mobile_number')
    CREATE_ACCOUNT_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')

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
    def enter_new_user_password(self, password):
        self.driver.find_element(*self.SIGNUP_PASSWORD_LOCATOR).send_keys(password)

    def enter_new_user_birth_day(self, day):
        dropdown = self.driver.find_element(*self.BIRTH_DAY_DROPDOWN_LOCATOR)
        Select(dropdown).select_by_visible_text(day)

    def enter_new_user_birth_month(self, month):
        dropdown = self.driver.find_element(*self.BIRTH_MONTH_DROPDOWN_LOCATOR)
        Select(dropdown).select_by_visible_text(month)

    def enter_new_user_birth_year(self, year):
        dropdown = self.driver.find_element(*self.BIRTH_YEAR_DROPDOWN_LOCATOR)
        Select(dropdown).select_by_visible_text(year)

    def enter_new_user_full_birthdate(self, day, month, year):
        self.enter_new_user_birth_day(day)
        self.enter_new_user_birth_month(month)
        self.enter_new_user_birth_year(year)

    def select_receive_newsletter(self):
        self.driver.find_element(*self.NEWSLETTER_CHECKBOX_LOCATOR).click()

    def select_special_offers(self):
        self.driver.find_element(*self.OPT_IN_CHECKBOX_LOCATOR).click()

    def select_optional_opt_ins(self):
        self.select_receive_newsletter()
        self.select_special_offers()






