# Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define page class
class HomePage:

    # Define Locators as class attributes
    LOGO_LOCATOR = (By.CSS_SELECTOR, ".logo img")
    SIGNUP_LOGIN_LINK_LOCATOR = (By.LINK_TEXT, 'Signup / Login')
    LOGGED_IN_USER_LOCATOR = (By.XPATH , '//a[contains(., "Logged in as")]')
    DELETE_ACCOUNT_LINK_LOCATOR = (By.LINK_TEXT, 'Delete Account')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to use page's logo to check if the home page is visible
    def is_page_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGO_LOCATOR)
        )

    # Method to click the 'Signup/Login' link at the top of the home page
    def click_signup_login_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN_LINK_LOCATOR)
        ).click()

    # Method to check if 'Logged-in user' message is present
    def is_logged_in_user_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_USER_LOCATOR)
        )

    # Method to retrieve the displayed user's name
    def get_logged_in_username(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_USER_LOCATOR)
        )
        return element.find_element(By.TAG_NAME, "b").text

    # Method to click on the Delete Account link
    def click_delete_account(self):
        self.driver.find_element(*self.DELETE_ACCOUNT_LINK_LOCATOR).click()