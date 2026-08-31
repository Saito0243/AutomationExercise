import data
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage


def test_valid_user_login(driver):

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

    # 5. Verify 'Login to your account' is visible
    assert signup_login_page.is_login_to_account_visible()

    # 6. Enter correct email address and password
    signup_login_page.enter_return_user_info(data.LOGIN_EMAIL, data.PASSWORD)

    # 7. Click 'login' button
    signup_login_page.click_login_button()

    # 16. Verify that 'Logged in as username' is visible
    assert home_page.is_logged_in_user_visible()

    # Check that user displayed is the correct user
    assert home_page.get_logged_in_username() == data.LOGIN_FULL_NAME
