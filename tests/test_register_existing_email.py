import data
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage

def test_register_user(driver):

    # 1: Launch Browser
    # 2. Navigate to url
    driver.get(data.BASE_URL)

    # Initialize home page object
    home_page = HomePage(driver)

    # 3. Verify that home page is visible successfully
    assert home_page.is_page_visible()

    # 4. Click on 'Signup / Login' button
    home_page.click_signup_login_link()

    # Initialize Signup / Login page object
    signup_login_page = SignupLoginPage(driver)

    # 5. Verify 'New User Signup!' is visible
    assert signup_login_page.is_new_user_signup_visible()

    # 6. Enter name and already registered email address
    signup_login_page.signup_new_user(data.LOGIN_FULL_NAME, data.LOGIN_EMAIL)

    # 7. Click 'Signup' button
    signup_login_page.click_signup_button()

    assert signup_login_page.is_email_already_exists_visible()