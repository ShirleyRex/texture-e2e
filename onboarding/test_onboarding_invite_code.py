import time
from selenium.webdriver.common.by import By

def test_select_hair_type():
    driver = setup_driver()
    driver.find_element(By.ID, "hair-type-curly").click()
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    assert "Next step" in driver.title
    teardown_driver(driver)

def test_multiple_hair_type_selections():
    driver = setup_driver()
    driver.find_element(By.ID, "hair-type-curly").click()
    driver.find_element(By.ID, "hair-type-kinky").click()
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    assert "Next step" in driver.title
    teardown_driver(driver)

def test_no_hair_type_selection():
    driver = setup_driver()
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    assert "Select at least one hair type" in driver.page_source
    teardown_driver(driver)

def test_select_hair_care_routine_frequency():
    driver = setup_driver()
    driver.find_element(By.ID, "frequency-weekly").click()
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    assert "Next step" in driver.title
    teardown_driver(driver)

def test_no_hair_care_routine_frequency_selection():
    driver = setup_driver()
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    assert "Select a hair care routine frequency" in driver.page_source
    teardown_driver(driver)

def test_hair_type_selection_page_load_time():
    driver = setup_driver()
    start_time = time.time()
    driver.get("http://localhost:3000/HairTypeSelection")
    load_time = time.time() - start_time
    assert load_time < 5
    teardown_driver(driver)

def test_hair_type_selection_page_accessibility():
    driver = setup_driver()
    driver.get("http://localhost:3000/HairTypeSelection")
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()
    teardown_driver(driver)

def test_account_creation_valid_details():
    driver = setup_driver()
    driver.find_element(By.ID, "first-name").send_keys("First")
    driver.find_element(By.ID, "surname").send_keys("Last")
    driver.find_element(By.ID, "username").send_keys("username")
    driver.find_element(By.ID, "country").send_keys("Country")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "create-account").click()
    time.sleep(2)
    assert "Dashboard" in driver.title
    teardown_driver(driver)

def test_account_creation_existing_username():
    driver = setup_driver()
    driver.find_element(By.ID, "first-name").send_keys("First")
    driver.find_element(By.ID, "surname").send_keys("Last")
    driver.find_element(By.ID, "username").send_keys("existingusername")
    driver.find_element(By.ID, "country").send_keys("Country")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "create-account").click()
    time.sleep(2)
    assert "Username already exists" in driver.page_source
    teardown_driver(driver)

def test_account_creation_invalid_password():
    driver = setup_driver()
    driver.find_element(By.ID, "first-name").send_keys("First")
    driver.find_element(By.ID, "surname").send_keys("Last")
    driver.find_element(By.ID, "username").send_keys("username")
    driver.find_element(By.ID, "country").send_keys("Country")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.ID, "create-account").click()
    time.sleep(2)
    assert "Password is too weak" in driver.page_source
    teardown_driver(driver)

def test_account_creation_empty_fields():
    driver = setup_driver()
    driver.find_element(By.ID, "create-account").click()
    time.sleep(2)
    assert "All fields are required" in driver.page_source
    teardown_driver(driver)

def test_password_visibility_toggle():
    driver = setup_driver()
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    driver.find_element(By.CLASS_NAME, "toggle-password-visibility").click()
    assert password_field.get_attribute("type") == "text"
    driver.find_element(By.CLASS_NAME, "toggle-password-visibility").click()
    assert password_field.get_attribute("type") == "password"
    teardown_driver(driver)

def test_account_creation_page_load_time():
    driver = setup_driver()
    start_time = time.time()
    driver.get("http://localhost:3000/AccountCreation")
    load_time = time.time() - start_time
    assert load_time < 5
    teardown_driver(driver)

def test_account_creation_page_accessibility():
    driver = setup_driver()
    driver.get("http://localhost:3000/AccountCreation")
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()
    teardown_driver(driver)