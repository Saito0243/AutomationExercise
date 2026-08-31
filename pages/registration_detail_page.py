# Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationDetailPage:

    # Declare locators as class attributes
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

    # Method to verify that 'ENTER ACCOUNT INFORMATION' is visible
    def enter_acct_info_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ENTER_ACCT_INFO_LOCATOR)
        )

    # Method to select Mr as the user's title
    def select_user_title(self):
        self.driver.find_element(*self.TITLE_MR_RADIO_LOCATOR).click()

    # Method to enter a password for the new user
    def enter_new_user_password(self, password):
        self.driver.find_element(*self.SIGNUP_PASSWORD_LOCATOR).send_keys(password)

    # Method to select the day of birth from the dropdown
    def enter_new_user_birth_day(self, day):
        dropdown = self.driver.find_element(*self.BIRTH_DAY_DROPDOWN_LOCATOR)
        Select(dropdown).select_by_visible_text(day)

    # Method to select the month of birth from the dropdown
    def enter_new_user_birth_month(self, month):
        dropdown = self.driver.find_element(*self.BIRTH_MONTH_DROPDOWN_LOCATOR)
        Select(dropdown).select_by_visible_text(month)

    # Method to select the year of birth from the dropdown
    def enter_new_user_birth_year(self, year):
        dropdown = self.driver.find_element(*self.BIRTH_YEAR_DROPDOWN_LOCATOR)
        Select(dropdown).select_by_visible_text(year)

    # Combining methods to enter the entire birthdate
    def enter_new_user_full_birthdate(self, day, month, year):
        self.enter_new_user_birth_day(day)
        self.enter_new_user_birth_month(month)
        self.enter_new_user_birth_year(year)

    def select_receive_newsletter(self):
        self.driver.find_element(*self.NEWSLETTER_CHECKBOX_LOCATOR).click()

    def select_special_offers(self):
        self.driver.find_element(*self.OPT_IN_CHECKBOX_LOCATOR).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT_LOCATOR).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT_LOCATOR).send_keys(last_name)

    def enter_company(self, company):
        self.driver.find_element(*self.COMPANY_INPUT_LOCATOR).send_keys(company)

    def enter_address_line1(self, address1):
        self.driver.find_element(*self.ADDRESS_1_INPUT_LOCATOR).send_keys(address1)

    def enter_address_line2(self, address2):
        self.driver.find_element(*self.ADDRESS_2_INPUT_LOCATOR).send_keys(address2)

    def select_country(self, country):
        dropdown = self.driver.find_element(*self.COUNTRY_DROPDOWN_LOCATOR)
        Select(dropdown).select_by_visible_text(country)

    def enter_state(self, state):
        self.driver.find_element(*self.STATE_INPUT_LOCATOR).send_keys(state)

    def enter_city(self, city):
        self.driver.find_element(*self.CITY_INPUT_LOCATOR).send_keys(city)

    def enter_zip_code(self, zip_code):
        self.driver.find_element(*self.ZIP_CODE_INPUT_LOCATOR).send_keys(zip_code)

    def enter_mobile_number(self, mobile_number):
        self.driver.find_element(*self.MOBILE_NUMBER_INPUT_LOCATOR).send_keys(mobile_number)

    def enter_address_info(self, address):
        self.enter_first_name(address["first_name"])
        self.enter_last_name(address["last_name"])
        self.enter_company(address["company"])
        self.enter_address_line1(address["address1"])
        self.enter_address_line2(address["address2"])
        self.select_country(address["country"])
        self.enter_state(address["state"])
        self.enter_city(address["city"])
        self.enter_zip_code(address["zip_code"])
        self.enter_mobile_number(address["mobile_number"])

    def click_create_account_button(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON_LOCATOR).click()




