import time
from selenium.webdriver.common.by import By

def test_request_invite_code_valid_email(driver):
    driver.get("http://localhost:3000/Onboarding")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validemail@example.com")
    time.sleep(5)
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    #assert "Confirmation message" in driver.page_source

def test_request_invite_code_invalid_email(driver):
    driver.get("http://localhost:3000/Onboarding")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("invalidemail")
    time.sleep(5)
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    #assert "Invalid email format" in driver.page_source

def test_request_invite_code_empty_email(driver):
    driver.get("http://localhost:3000/Onboarding")
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    #assert "Email is required" in driver.page_source

def test_sign_in_link(driver):
    driver.get("http://localhost:3000/Onboarding")
    driver.find_element(By.LINK_TEXT, "Sign in!").click()
    time.sleep(5)
    #assert "Texture Hair" in driver.title

def test_broken_sign_in_link(driver):
    driver.get("http://localhost:3000/Onboarding")
    driver.find_element(By.LINK_TEXT, "Sign in!").click()
    time.sleep(10)
    #assert "404" not in driver.title

def test_invite_code_page_load_time(driver):
    start_time = time.time()
    driver.get("http://localhost:3000/Onboarding")
    load_time = time.time() - start_time
    assert load_time < 5

def test_invite_code_page_accessibility(driver):
    driver.get("http://localhost:3000/Onboarding")
    input_elements = driver.find_elements(By.TAG_NAME, "input")
    email_input = input_elements[0]
    assert email_input.is_displayed(), "Email input field is not displayed"
    time.sleep(10)

def test_confirmation_message(driver):
    driver.get("http://localhost:3000/Onboarding")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validemail@example.com")
    time.sleep(5)
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    assert "Invite code has been successfully sent!" in driver.page_source

def test_sign_in_link_from_confirmation(driver):
    driver.get("http://localhost:3000/Onboarding")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validemail@example.com")
    time.sleep(5)
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Sign in!").click()
    time.sleep(5)
    #assert "Sign-in Page" in driver.title

def test_broken_sign_in_link_on_confirmation(driver):
    driver.get("http://localhost:3000/Onboarding")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validemail@example.com")
    time.sleep(5)
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Sign in!").click()
    time.sleep(5)
    #assert "404" not in driver.title

def test_email_receipt_of_invite_code(driver):
    driver.get("http://localhost:3000/Onboarding")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validemail@example.com")
    time.sleep(5)
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    # Check the email inbox manually or use an email API

def test_confirmation_page_load_time(driver):
    driver.get("http://localhost:3000/Onboarding")
    start_time = time.time()
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validemail@example.com")
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    load_time = time.time() - start_time
    assert load_time < 5

def test_confirmation_page_accessibility(driver):
    driver.get("http://localhost:3000/Onboarding")
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys("validemail@example.com")
    request_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()
