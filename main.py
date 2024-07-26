from common.setup_teardown import setup_driver, teardown_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from onboarding.test_onboarding import (test_request_invite_code_valid_email, test_request_invite_code_invalid_email,
                                        test_request_invite_code_empty_email, test_sign_in_link,
                                        test_broken_sign_in_link,
                                        test_invite_code_page_load_time, test_invite_code_page_accessibility,
                                        test_confirmation_message, test_sign_in_link_from_confirmation,
                                        test_broken_sign_in_link_on_confirmation, test_email_receipt_of_invite_code,
                                        test_confirmation_page_load_time, test_confirmation_page_accessibility)

from onboarding.test_onboarding_return import (test_select_hair_type)

from sign_in.test_sign_in import (test_sign_in_with_valid_credentials, test_invalid_email_format,
                                  test_incorrect_password,
                                  test_empty_email_field, test_empty_password_field,
                                  test_empty_email_and_password_fields,
                                  test_email_with_spaces, test_password_visibility_toggle, test_broken_sign_in_button,
                                  test_unresponsive_sign_in_button, test_sign_up_link, test_broken_sign_up_link,
                                  test_unresponsive_sign_up_link, test_sign_in_page_load_time,
                                  test_broken_images_on_sign_in_page,
                                  test_sign_in_page_accessibility, test_email_with_special_characters,
                                  test_password_with_special_characters,
                                  test_remember_me_functionality, test_sign_in_with_non_existent_account)

from user_feed.test_user_feed import (test_feed_page_load_time, test_like_post, test_feed_page_accessibility)


def driver():
    driver = setup_driver()
    return driver
    # teardown_driver(driver)


if __name__ == "__main__":
    # test_request_invite_code_valid_email(driver())
    # test_request_invite_code_invalid_email(driver())
    # test_request_invite_code_empty_email(driver())
    # test_broken_sign_in_link(driver())
    # test_invite_code_page_load_time(driver())
    # test_invite_code_page_accessibility(driver())
    # test_confirmation_message(driver())
    # test_sign_in_link_from_confirmation(driver())
    # test_broken_sign_in_link_on_confirmation(driver())
    # test_email_receipt_of_invite_code(driver())
    # test_confirmation_page_load_time(driver())
    # test_confirmation_page_accessibility(driver())
    # test_sign_in_with_valid_credentials(driver())
    # test_invalid_email_format(driver())
    # test_incorrect_password(driver())
    # test_empty_email_field(driver())
    # test_empty_password_field(driver())
    # test_empty_email_and_password_fields(driver())
    # test_email_with_spaces(driver())
    # test_password_visibility_toggle(driver())
    # test_broken_sign_in_button(driver())
    # test_unresponsive_sign_in_button(driver())
    # test_sign_up_link(driver())
    # test_broken_sign_up_link(driver())
    # test_unresponsive_sign_up_link(driver())
    # test_sign_in_page_load_time(driver())
    # test_broken_images_on_sign_in_page(driver())
    # test_sign_in_page_accessibility(driver())
    # test_email_with_special_characters(driver())
    # test_password_with_special_characters(driver())
    # test_remember_me_functionality(driver())
    # test_sign_in_with_non_existent_account(driver())
    # test_select_hair_type(driver())
    # test_feed_page_load_time(driver())
    test_like_post(driver())
    # test_feed_page_accessibility(driver())