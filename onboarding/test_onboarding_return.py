import time
from selenium.webdriver.common.by import By


def test_select_hair_type(driver):
    driver.get("http://localhost:3000/HairTypeSelection")
    hair_type = driver.find_elements(By.TAG_NAME, "input")[0].click()
    time.sleep(2)
    continue_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(2)
    assert "Next step" in driver.title


def test_multiple_hair_type_selections(driver):
    driver.get("http://localhost:3000/HairTypeSelection")
    hair_type1 = driver.find_elements(By.TAG_NAME, "input")[0].click()
    time.sleep(2)
    hair_type2 = driver.find_elements(By.TAG_NAME, "input")[1].click()
    time.sleep(2)
    continue_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(2)
    assert "Next step" in driver.title


def test_no_hair_type_selection(driver):
    driver.get("http://localhost:3000/HairTypeSelection")
    continue_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(2)
    assert "Select at least one hair type" in driver.page_source


def test_select_hair_care_routine_frequency(driver):
    driver.get("http://localhost:3000/HairTypeSelection")
    frequency = driver.find_elements(By.TAG_NAME, "input")[2].click()
    time.sleep(2)
    continue_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(2)
    assert "Next step" in driver.title


def test_no_hair_care_routine_frequency_selection(driver):
    driver.get("http://localhost:3000/HairTypeSelection")
    continue_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(2)
    assert "Select a hair care routine frequency" in driver.page_source


def test_hair_type_selection_page_load_time(driver):
    start_time = time.time()
    driver.get("http://localhost:3000/HairTypeSelection")
    load_time = time.time() - start_time
    assert load_time < 5


def test_hair_type_selection_page_accessibility(driver):
    driver.get("http://localhost:3000/HairTypeSelection")
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()


def test_account_creation_valid_details(driver):
    driver.get("http://localhost:3000/AccountCreation")
    first_name = driver.find_elements(By.TAG_NAME, "input")[0].send_keys("First")
    time.sleep(2)
    surname = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("Last")
    time.sleep(2)
    username = driver.find_elements(By.TAG_NAME, "input")[2].send_keys("username")
    time.sleep(2)
    country = driver.find_elements(By.TAG_NAME, "input")[3].send_keys("Country")
    time.sleep(2)
    password = driver.find_elements(By.TAG_NAME, "input")[4].send_keys("Password123")
    time.sleep(2)
    create_account_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(5)
    assert "Dashboard" in driver.title


def test_account_creation_existing_username(driver):
    driver.get("http://localhost:3000/AccountCreation")
    first_name = driver.find_elements(By.TAG_NAME, "input")[0].send_keys("First")
    time.sleep(2)
    surname = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("Last")
    time.sleep(2)
    username = driver.find_elements(By.TAG_NAME, "input")[2].send_keys("existingusername")
    time.sleep(2)
    country = driver.find_elements(By.TAG_NAME, "input")[3].send_keys("Country")
    time.sleep(2)
    password = driver.find_elements(By.TAG_NAME, "input")[4].send_keys("Password123")
    time.sleep(2)
    create_account_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(5)
    assert "Username already exists" in driver.page_source


def test_account_creation_invalid_password(driver):
    driver.get("http://localhost:3000/AccountCreation")
    first_name = driver.find_elements(By.TAG_NAME, "input")[0].send_keys("First")
    time.sleep(2)
    surname = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("Last")
    time.sleep(2)
    username = driver.find_elements(By.TAG_NAME, "input")[2].send_keys("username")
    time.sleep(2)
    country = driver.find_elements(By.TAG_NAME, "input")[3].send_keys("Country")
    time.sleep(2)
    password = driver.find_elements(By.TAG_NAME, "input")[4].send_keys("12345")
    time.sleep(2)
    create_account_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(5)
    assert "Password is too weak" in driver.page_source


def test_account_creation_empty_fields(driver):
    driver.get("http://localhost:3000/AccountCreation")
    create_account_button = driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(5)
    assert "All fields are required" in driver.page_source


def test_password_visibility_toggle(driver):
    driver.get("http://localhost:3000/AccountCreation")
    password_input = driver.find_elements(By.TAG_NAME, "input")[4].send_keys("Password123")
    time.sleep(2)
    toggle_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(2)
    assert driver.find_elements(By.TAG_NAME, "input")[4].get_attribute("type") == "text"
    toggle_button = driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(2)
    assert driver.find_elements(By.TAG_NAME, "input")[4].get_attribute("type") == "password"


def test_account_creation_page_load_time(driver):
    start_time = time.time()
    driver.get("http://localhost:3000/AccountCreation")
    load_time = time.time() - start_time
    assert load_time < 5


def test_account_creation_page_accessibility(driver):
    driver.get("http://localhost:3000/AccountCreation")
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()
