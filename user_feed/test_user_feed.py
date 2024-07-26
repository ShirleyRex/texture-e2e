import time
from selenium.webdriver.common.by import By
from utils.functions import sign_in, get_valid_credentials


def test_feed_page_load_time(driver):
    url, email, password = get_valid_credentials()
    sign_in(driver, url, email, password, should_sleep=True)
    driver.get("http://localhost:3000/profile")
    time.sleep(2)
    assert driver.current_url == "http://localhost:3000/profile"
    start_time = time.time()
    driver.get("http://localhost:3000/userfeed")
    assert driver.current_url == "http://localhost:3000/userfeed"
    load_time = time.time() - start_time
    assert load_time < 1


def test_feed_page_accessibility(driver):
    driver.get("http://localhost:3000/userfeed")
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()


def test_create_new_post(driver):
    driver.get("http://localhost:3000/userfeed")
    create_post_button = driver.find_elements(By.TAG_NAME, "button")[
        0].click()  # Assuming the first button is for creating a new post
    time.sleep(2)
    post_input = driver.find_elements(By.TAG_NAME, "textarea")[0].send_keys("This is a new post.")
    time.sleep(2)
    submit_post_button = driver.find_elements(By.TAG_NAME, "button")[
        1].click()  # Assuming the second button is to submit the post
    time.sleep(5)
    assert "This is a new post." in driver.page_source


def test_like_post(driver):
    url, email, password = get_valid_credentials()
    sign_in(driver, url, email, password, should_sleep=True)
    driver.get("http://localhost:3000/userfeed")
    like_button = driver.find_elements(By.TAG_NAME, "button")[2].click()
    time.sleep(10)
    # assert "Liked" in driver.page_source  # Assuming the text "Liked" appears after liking a post


def test_comment_on_post(driver):
    driver.get("http://localhost:3000/userfeed")
    comment_button = driver.find_elements(By.TAG_NAME, "button")[
        3].click()  # Assuming the fourth button is for commenting on a post
    time.sleep(2)
    comment_input = driver.find_elements(By.TAG_NAME, "textarea")[0].send_keys("This is a comment.")
    time.sleep(2)
    submit_comment_button = driver.find_elements(By.TAG_NAME, "button")[
        4].click()  # Assuming the fifth button is to submit the comment
    time.sleep(5)
    assert "This is a comment." in driver.page_source


def test_share_post(driver):
    driver.get("http://localhost:3000/userfeed")
    share_button = driver.find_elements(By.TAG_NAME, "button")[
        5].click()  # Assuming the sixth button is for sharing a post
    time.sleep(2)
    assert "Shared" in driver.page_source  # Assuming the text "Shared" appears after sharing a post


def test_delete_post(driver):
    driver.get("http://localhost:3000/userfeed")
    delete_button = driver.find_elements(By.TAG_NAME, "button")[
        6].click()  # Assuming the seventh button is for deleting a post
    time.sleep(2)
    confirm_delete_button = driver.find_elements(By.TAG_NAME, "button")[
        7].click()  # Assuming the eighth button is to confirm deletion
    time.sleep(5)
    assert "Post deleted" in driver.page_source  # Assuming the text "Post deleted" appears after deleting a post
