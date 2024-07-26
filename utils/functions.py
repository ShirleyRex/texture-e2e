import time
from selenium.webdriver.common.by import By


def sign_in(driver, url, email, password, should_sleep=False):
    driver.get(url)
    email_input = driver.find_element(By.TAG_NAME, "input").send_keys(email)
    if should_sleep:
        time.sleep(2)
    password_input = driver.find_elements(By.TAG_NAME, "input")[1].send_keys(password)
    if should_sleep:
        time.sleep(2)
    request_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    if should_sleep:
        time.sleep(5)


def get_valid_credentials():
    url = "http://localhost:3000/sign-in"
    email = "shirley.abaegbu@gmail.com"
    password = "@Testtexture24"

    return url, email, password
