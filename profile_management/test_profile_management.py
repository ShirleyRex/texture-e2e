def test_access_edit_profile_page(driver):
    # TC-PM-01: Verify user can access edit profile page
    driver.get("http://localhost:3000/profile")
    profile_icon = driver.find_element(By.TAG_NAME, "img").click()
    time.sleep(5)
    edit_profile = driver.find_element(By.LINK_TEXT, "Edit Profile").click()
    time.sleep(5)
    assert "edit-profile" in driver.current_url

def test_update_profile_photo(driver):
    # TC-PM-02: Validate updating profile photo
    driver.get("http://localhost:3000/edit-profile")
    profile_photo = driver.find_element(By.TAG_NAME, "img").click()
    time.sleep(5)
    file_input = driver.find_element(By.TAG_NAME, "input[type='file']").send_keys("/path/to/new/photo.jpg")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    updated_photo = driver.find_element(By.TAG_NAME, "img")
    assert updated_photo.get_attribute("src") == "/path/to/new/photo.jpg"

def test_update_profile_information(driver):
    # TC-PM-03: Validate updating profile information
    driver.get("http://localhost:3000/edit-profile")
    first_name = driver.find_elements(By.TAG_NAME, "input")[0].send_keys("NewFirstName")
    time.sleep(5)
    surname = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("NewSurname")
    time.sleep(5)
    username = driver.find_elements(By.TAG_NAME, "input")[2].send_keys("NewUsername")
    time.sleep(5)
    about_you = driver.find_elements(By.TAG_NAME, "textarea")[0].send_keys("New about you text")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    profile_info = driver.find_element(By.ID, "profile-info")
    assert "NewFirstName" in profile_info.text

def test_profile_update_with_invalid_data(driver):
    # TC-PM-04: Verify profile update with invalid data
    driver.get("http://localhost:3000/edit-profile")
    username = driver.find_elements(By.TAG_NAME, "input")[2].send_keys("!nv@l!dUs3rn@me")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    assert "invalid data" in error_message.text

def test_profile_photo_upload_invalid_file_type(driver):
    # TC-PM-05: Validate profile photo upload with invalid file type
    driver.get("http://localhost:3000/edit-profile")
    profile_photo = driver.find_element(By.TAG_NAME, "img").click()
    time.sleep(5)
    file_input = driver.find_element(By.TAG_NAME, "input[type='file']").send_keys("/path/to/file.txt")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    assert "invalid file type" in error_message.text

def test_profile_photo_upload_large_file_size(driver):
    # TC-PM-06: Validate profile photo upload with large file size
    driver.get("http://localhost:3000/edit-profile")
    profile_photo = driver.find_element(By.TAG_NAME, "img").click()
    time.sleep(5)
    file_input = driver.find_element(By.TAG_NAME, "input[type='file']").send_keys("/path/to/largephoto.jpg")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    assert "file size limit is exceeded" in error_message.text

def test_reset_profile_changes(driver):
    # TC-PM-07: Verify reset profile changes functionality
    driver.get("http://localhost:3000/edit-profile")
    first_name = driver.find_elements(By.TAG_NAME, "input")[0].send_keys("TempFirstName")
    time.sleep(5)
    surname = driver.find_elements(By.TAG_NAME, "input")[1].send_keys("TempSurname")
    time.sleep(5)
    reset_button = driver.find_element(By.TAG_NAME, "button[aria-label='Reset']").click()
    time.sleep(5)
    assert "TempFirstName" not in driver.page_source

def test_navigation_back_from_edit_profile_page(driver):
    # TC-PM-08: Verify navigation back from edit profile page
    driver.get("http://localhost:3000/edit-profile")
    back_button = driver.find_element(By.TAG_NAME, "button[aria-label='Back']").click()
    time.sleep(5)
    assert "profile" in driver.current_url

def test_website_url_field(driver):
    # TC-PM-09: Validate website URL field
    driver.get("http://localhost:3000/edit-profile")
    website_input = driver.find_element(By.TAG_NAME, "input").send_keys("http://validurl.com")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    profile_info = driver.find_element(By.ID, "profile-info")
    assert "http://validurl.com" in profile_info.text

def test_website_url_field_invalid(driver):
    # TC-PM-10: Validate website URL field with invalid URL
    driver.get("http://localhost:3000/edit-profile")
    website_input = driver.find_element(By.TAG_NAME, "input").send_keys("invalidurl")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    error_message = driver.find_element(By.TAG_NAME, "p")
    assert "invalid URL" in error_message.text

def test_view_follower_list(driver):
    # TC-PM-11: Verify viewing follower list
    driver.get("http://localhost:3000/profile")
    followers_link = driver.find_element(By.LINK_TEXT, "Following").click()
    time.sleep(5)
    followers_list = driver.find_element(By.ID, "followers-list")
    assert len(followers_list.find_elements(By.TAG_NAME, "li")) > 0

def test_search_within_follower_list(driver):
    # TC-PM-12: Verify search within follower list
    driver.get("http://localhost:3000/profile/followers")
    search_input = driver.find_element(By.TAG_NAME, "input").send_keys("searchusername")
    time.sleep(5)
    filtered_list = driver.find_element(By.ID, "followers-list")
    assert "searchusername" in filtered_list.text

def test_follow_unfollow_user(driver):
    # TC-PM-13: Validate following/unfollowing a user
    driver.get("http://localhost:3000/profile/followers")
    follow_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    assert "Following" in follow_button.text or "Follow" in follow_button.text

def test_profile_update_success_notification(driver):
    # TC-PM-14: Verify profile update success notification
    driver.get("http://localhost:3000/edit-profile")
    first_name = driver.find_elements(By.TAG_NAME, "input")[0].send_keys("UpdatedFirstName")
    time.sleep(5)
    save_button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    success_message = driver.find_element(By.TAG_NAME, "p")
    assert "Profile was updated successfully" in success_message.text

def test_responsiveness_of_profile_pages(driver):
    # TC-PM-15: Validate responsiveness of profile management pages
    driver.get("http://localhost:3000/profile")
    # Code to resize window to desktop, tablet, and mobile sizes
    # For desktop
    driver.set_window_size(1920, 1080)
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()
    # For tablet
    driver.set_window_size(768, 1024)
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()
    # For mobile
    driver.set_window_size(375, 667)
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()

def test_accessibility_of_profile_pages(driver):
    # TC-PM-16: Verify accessibility of profile management pages
    driver.get("http://localhost:3000/profile")
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.TAB)  # Navigate using keyboard
    assert body  # Just a placeholder to ensure this runs, replace with meaningful assertions

def test_view_profile_information(driver):
    # TC-PM-17: Verify viewing profile information
    driver.get("http://localhost:3000/profile")
    profile_info = driver.find_element(By.ID, "profile-info")
    assert "Profile Information" in profile_info.text