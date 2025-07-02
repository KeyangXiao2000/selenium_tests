import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup():
    driver = webdriver.Chrome()
    driver.get("https://keyangxiao2000.github.io/coursera-react-final-project/")
    return driver

def teardown(driver):
    driver.quit()

def test_site_title():
    driver = setup()

    title = driver.title
    assert title == "E-Plant"

    teardown(driver)

def test_plant_titles():
    driver = setup()

    categories = driver.find_elements(By.CSS_SELECTOR, ".product-grid > div")
    assert len(categories) == 5
    assert categories[0].find_element(By.CSS_SELECTOR, "h1").get_attribute("innerHTML") == "Air Purifying Plants"

    lmps = categories[4].find_elements(By.CSS_SELECTOR, ".product-card")
    assert len(lmps) == 6

    zz = lmps[0].find_element(By.CSS_SELECTOR, ".product-title")
    assert zz.get_attribute("innerHTML") == "ZZ Plant"

    teardown(driver)

def test_buttons():
    driver = setup()

    get_started_btn = driver.find_element(By.CLASS_NAME, "get-started-button")
    get_started_btn.click()
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-list-container")))

    hypers = driver.find_elements(By.CSS_SELECTOR, ".product-list-container a")
    assert len(hypers) == 3

    cart_btn = hypers[2]
    wait.until(EC.element_to_be_clickable(cart_btn))
    cart_btn.click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-container")))

    checkout_btn = driver.find_element(By.CLASS_NAME, "get-started-button1")
    checkout_btn.click()
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    assert alert.text == "Functionality to be added for future reference"

    teardown(driver)
