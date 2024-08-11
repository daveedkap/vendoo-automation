from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from main import automate_crosslisting

# Setup the WebDriver
def setup_driver():
    driver = webdriver.Chrome()
    return driver

# Login to Vendoo
def login(driver, email, password):
    driver.get("https://web.vendoo.co/login")
    time.sleep(1)
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    username_field.send_keys(email)
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()
    time.sleep(1)

# Test Grailed crosslisting
def test_grailed(driver):
    driver.get("https://web.vendoo.co/app/item/Xl6YXpLpyavswcXdrW2m?marketplace=grailed")
    time.sleep(1)
    automate_crosslisting(driver)

# Run all tests
def run_tests():
    driver = setup_driver()
    try:
        login(driver, "dkaplanskybrimmer@gmail.com", "passwordfortesting")
        test_grailed(driver)
        # Add more tests as needed, e.g., test_depop(driver), etc.
    finally:
        driver.quit()

# Automatically run tests when the script is executed
if __name__ == "__main__":
    run_tests()
