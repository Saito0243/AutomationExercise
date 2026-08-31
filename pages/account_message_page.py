# Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define page class
class AccountMessagePage:

    # Define locators as class attributes
    ACCT_CREATED_LOCATOR = (By.CSS_SELECTOR, '[data-qa="account-created"]')
    ACCT_DELETED_LOCATOR = (By.CSS_SELECTOR, '[data-qa="account-deleted"]')
    CONTINUE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[data-qa="continue-button"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to check if 'Account Created!' is visible
    def is_acct_created_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCT_CREATED_LOCATOR)
        )

    # Method to click the continue button
    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON_LOCATOR).click()

    # Method to check if 'Account Deleted!' is visible
    def is_account_deleted_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCT_DELETED_LOCATOR)
        )

