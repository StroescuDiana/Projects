
class LoginPageObjects:
    username_field_xpath = "//input[@id='username']"
    password_field_xpath = "//input[@id='password'][@name='password']"
    submit_login_button_xpath = "//button[@class='btn'][@id='submit']"
    successfully_logged_in_url = "https://practicetestautomation.com/logged-in-successfully/"
    log_in_page_url = "https://practicetestautomation.com/practice-test-login/"
    successfully_logged_in_text = "Logged In Successfully"
    logged_in_successfully_xpath = "//h1[@class='post-title']"
    log_out_button_link = "Log out"
    login_data_invalid_label_xpath = "//div[@id='error']"
    username_invalid_expected_message = "Your username is invalid!"
    password_invalid_expected_message = "Your password is invalid!"
    valid_username = "student"
    valid_password = "Password123"
    invalid_username = "studenta"
    invalid_password = "password123"