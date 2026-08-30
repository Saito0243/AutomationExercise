# Define Locators as class attributes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    # Define Locators as class attributes
    LOGO_LOCATOR = (By.CSS_SELECTOR, ".logo img")
    SIGNUP_LOGIN_LINK_LOCATOR = (By.LINK_TEXT, 'Signup / Login')

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