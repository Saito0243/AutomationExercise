import data
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.registration_detail_page import RegistrationDetailPage
from pages.account_message_page import AccountMessagePage

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

    # 6. Enter name and email address
    signup_login_page.signup_new_user(data.SIGNUP_FULL_NAME, data.SIGNUP_EMAIL)

    # 7. Click 'Signup' button
    signup_login_page.click_signup_button()
    
    # Initialize registration detail page object
    registration_detail_page = RegistrationDetailPage(driver)

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert registration_detail_page.enter_acct_info_visible()

    # 9. Fill details: Title, Name, Email, Password, Date of birth
    registration_detail_page.select_user_title()
    registration_detail_page.enter_new_user_password(data.PASSWORD)
    registration_detail_page.enter_new_user_full_birthdate(data.BIRTH_DAY, data.BIRTH_MONTH, data.BIRTH_YEAR)

    # 10. Select checkbox 'Sign up for our newsletter!'
    registration_detail_page.select_receive_newsletter()

    # 11. Select checkbox 'Receive special offers from our partners!'
    registration_detail_page.select_special_offers()

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    registration_detail_page.enter_address_info(data.ADDRESS_INFO)

    # 13. Click 'Create Account button'
    registration_detail_page.click_create_account_button()

    # Initialize Account Created page object
    account_message_page = AccountMessagePage(driver)

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    assert account_message_page.is_acct_created_visible()

    # 15. Click 'Continue' button
    account_message_page.click_continue_button()

    # 16. Verify that 'Logged in as username' is visible
    assert home_page.is_logged_in_user_visible()

    # Check that user displayed is the correct user
    assert home_page.get_logged_in_username() == data.LOGIN_FULL_NAME

    # 17. Click 'Delete Account' button
    home_page.click_delete_account()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert account_message_page.is_account_deleted_visible()
    account_message_page.click_continue_button()


