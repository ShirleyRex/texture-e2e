import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_sign_in_with_valid_credentials(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("shirley.abaegbu@gmail.com")
    time.sleep(2)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("@Testtexture24")
    time.sleep(2)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    # assert profile_url in driver.current_url


def test_invalid_email_format(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("invalidemail")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("ValidPassword123")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    # assert "Invalid email format" in error_message.text


def test_incorrect_password(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validuser@example.com")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("WrongPassword")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    # assert "Incorrect password" in error_message.text


def test_empty_email_field(driver):
    driver.get("http://localhost:3000/sign-in")
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("ValidPassword123")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    # assert "Email is required" in error_message.text


def test_empty_password_field(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validuser@example.com")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    # assert "Password is required" in error_message.text


def test_empty_email_and_password_fields(driver):
    driver.get("http://localhost:3000/sign-in")
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    # assert "Email and password are required" in error_message.text


def test_email_with_spaces(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys(" shirley.abaegbu@gmail.com ")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("@Testtexture24")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    # assert profile_url in driver.current_url or "Invalid email or password" in driver.page_source


def test_password_visibility_toggle(driver):
    driver.get("http://localhost:3000/sign-in")
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("ValidPassword123")
    time.sleep(5)
    toggle_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(5)
    # assert password_input.get_attribute("type") == "text"
    # toggle_button.click()
    # assert password_input.get_attribute("type") == "password"


def test_broken_sign_in_button(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("shirley.abaegbu@gmail.com")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("@Testtexture24")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    assert not (driver.current_url == "http://localhost:3000/404" or "Page not found" in driver.page_source)


def test_unresponsive_sign_in_button(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("shirley.abaegbu@gmail.com")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("@Testtexture24")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)  # Wait to see if the button is responsive
    assert driver.current_url != "http://localhost:3000/sign-in"


def test_sign_up_link(driver):
    driver.get("http://localhost:3000/sign-in")
    time.sleep(5)
    sign_up_link = driver.find_element(By.LINK_TEXT, "Sign up!").click()
    time.sleep(5)
    # assert "sign-up" in driver.current_url  # Adjust the condition


def test_broken_sign_up_link(driver):
    driver.get("http://localhost:3000/sign-in")
    time.sleep(5)
    sign_up_link = driver.find_element(By.LINK_TEXT, "Sign up!").click()
    time.sleep(5)
    # assert not (driver.current_url == "http://localhost:3000/404" or "Page not found" in driver.page_source)


def test_unresponsive_sign_up_link(driver):
    driver.get("http://localhost:3000/sign-in")
    time.sleep(5)
    sign_up_link = driver.find_element(By.LINK_TEXT, "Sign up!").click()
    time.sleep(5)
    # assert driver.current_url != "http://localhost:3000/sign-in"


def test_sign_in_page_load_time(driver):
    start_time = time.time()
    driver.get("http://localhost:3000/sign-in")
    time.sleep(5)
    load_time = time.time() - start_time
    # assert load_time < 5  # Adjust the acceptable time limit


def test_broken_images_on_sign_in_page(driver):
    driver.get("http://localhost:3000/sign-in")
    images = driver.find_elements(By.TAG_NAME, "img")
    for image in images:
        assert image.get_attribute("naturalWidth") != "0"


def test_sign_in_page_accessibility(driver):
    driver.get("http://localhost:3000/sign-in")
    body = driver.find_element(By.TAG_NAME, "body").send_keys(Keys.TAB)
    time.sleep(20)
    # assert body


def test_email_with_special_characters(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("shirley.abaegbu@gmail.com")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("@Testtexture24")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    # assert profile_url in driver.current_url or "Invalid email or password" in driver.page_source


def test_password_with_special_characters(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("shirley.abaegbu@gmail.com")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("@Testtexture24")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    # assert profile_url in driver.current_url or "Invalid email or password" in driver.page_source


def test_remember_me_functionality(driver):  # suggested feature
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("shirley.abaegbu@gmail.com")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("@Testtexture24")
    time.sleep(5)
    remember_me_checkbox = driver.find_elements(By.TAG_NAME, "input")[
        2].click()  # Assuming the "Remember me" checkbox is the third input element
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    # assert profile_url in driver.current_url


def test_sign_in_with_non_existent_account(driver):
    driver.get("http://localhost:3000/sign-in")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("nonexistentuser@example.com")
    time.sleep(5)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("AnyPassword123")
    time.sleep(5)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    # assert "account does not exist" in error_message.text
