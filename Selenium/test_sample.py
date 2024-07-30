import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


@pytest.fixture(scope="module")
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://artoftesting.com/samplesiteforselenium")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.quit()


# Link
def test_link(test_setup):
    link = driver.find_element(By.XPATH, "//a[text()='This is a link']")
    link.click()
    time.sleep(2)
    new_page_identifier = driver.find_element(By.TAG_NAME, "h1")
    assert new_page_identifier.text == "Sample Webpage for Automation Practice"
    time.sleep(3)


# Textbox
def test_textbox(test_setup):
    textbox = driver.find_element(By.ID, "fname")
    textbox.send_keys("Hello there")
    time.sleep(3)


# Button
def test_button(test_setup):
    button = driver.find_element(By.ID, "idOfButton")
    button.click()
    actions = ActionChains(driver)
    actions.move_to_element(button).perform()
    time.sleep(3)


# Double click Alert Box
def test_doubleclick_alert(test_setup):
    button = driver.find_element(By.ID, "dblClkBtn")
    actions = ActionChains(driver)
    actions.double_click(button).perform()
    time.sleep(2)
    txt = driver.switch_to.alert.text
    assert txt == "Hi! Art Of Testing, Here!"
    driver.switch_to.alert.accept()
    time.sleep(3)


# Radio Buttons
def test_radiobuttons(test_setup):
    male_radio = driver.find_element(By.ID, "male")
    male_radio.click()
    assert male_radio.is_selected()
    female_radio = driver.find_element(By.ID, "female")
    female_radio.click()
    assert female_radio.is_selected()
    assert not male_radio.is_selected()
    time.sleep(3)


# CheckBox
def test_checkbox(test_setup):
    check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for ele in check_box:
        ele.click()
        assert ele.is_selected()
    time.sleep(3)


# Dropdown
def test_dropdown(test_setup):
    dropdown = driver.find_element(By.ID, "testingDropdown")
    sel = Select(dropdown)
    sel.select_by_value("Performance")
    sel.select_by_visible_text("Database Testing")
    time.sleep(3)


# Alert Box
def test_alert_box(test_setup):
    driver.find_element(By.XPATH, "//button[text()='Generate Alert Box']").click()
    time.sleep(2)
    tx = driver.switch_to.alert.text
    assert tx == "Hi! Art Of Testing, Here!"
    driver.switch_to.alert.accept()
    time.sleep(3)


# Confirm Box
def test_confirm_box(test_setup):
    driver.find_element(By.XPATH, "//button[text()='Generate Confirm Box']").click()
    time.sleep(2)
    tx = driver.switch_to.alert.text
    assert tx == "Press a button!"
    driver.switch_to.alert.dismiss()
    time.sleep(3)
