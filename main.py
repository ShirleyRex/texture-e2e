from common.setup_teardown import setup_driver, teardown_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from onboarding.test_onboarding import (test_request_invite_code_valid_email, test_request_invite_code_invalid_email,
                                        test_request_invite_code_empty_email, test_sign_in_link, test_broken_sign_in_link,
                                        test_invite_code_page_load_time, test_invite_code_page_accessibility,
                                        test_confirmation_message, test_sign_in_link_from_confirmation,
                                        test_broken_sign_in_link_on_confirmation, test_email_receipt_of_invite_code,
                                        test_confirmation_page_load_time, test_confirmation_page_accessibility)

from sign_in.test_sign_in import (test_sign_in_with_valid_credentials, test_invalid_email_format)

def driver():
    driver = setup_driver()
    return driver
    # teardown_driver(driver)


if __name__ == "__main__":
    #test_request_invite_code_valid_email(driver())
    #test_request_invite_code_invalid_email(driver())
    #test_request_invite_code_empty_email(driver())
    #test_broken_sign_in_link(driver())
    #test_invite_code_page_load_time(driver())
    #test_invite_code_page_accessibility(driver())
    #test_confirmation_message(driver())
    #test_sign_in_link_from_confirmation(driver())
    #test_broken_sign_in_link_on_confirmation(driver())
    #test_email_receipt_of_invite_code(driver())
    #test_confirmation_page_load_time(driver())
    #test_confirmation_page_accessibility(driver())
    test_sign_in_with_valid_credentials(driver())
    #test_invalid_email_format(driver())

