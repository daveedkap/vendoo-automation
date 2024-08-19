from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options 
import time
from GrailedAutomation import GrailedAutomation

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
    grailed_login(driver)
    driver.get("https://web.vendoo.co/app/item/Xl6YXpLpyavswcXdrW2m?marketplace=grailed")
    time.sleep(1)
    
    # Instantiate the GrailedAutomation class and run the automation
    grailed_automation = GrailedAutomation(driver)
    grailed_automation.automate_crosslisting()

def grailed_login(driver):
    driver.get("https://www.grailed.com")
    # Click login button 
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "global-header-login-btn")))
    login_button.click()
    time.sleep(.5)
    # Click login with email button
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-cy='login-with-email']")))
    login_button.click()
    time.sleep(.5)
    # Click and enter email
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email_input.click()
    email_input.send_keys("luccapiconroura@gmail.com")
    # Click and enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password_input.click()
    password_input.send_keys("passwordfortesting")
    # Click final login button
    final_login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-cy='auth-login-submit']")))
    final_login_button.click()
    time.sleep(2)


def download_extension():
    try:
        options = webdriver.ChromeOptions()
        options.add_extension('vendoo-extension.crx')
        driver = webdriver.Chrome(options=options)

        print("Extension added to Chrome")
        time.sleep(1)
        return driver
    except Exception as e:
        print("Failed to add extension:", e)
        return None
    
# Run all tests
def run_tests():
    driver = setup_driver()
    driver = download_extension()
    if driver is not None:
        try:
            login(driver, "dkaplanskybrimmer@gmail.com", "passwordfortesting")
            test_grailed(driver)
            # Add more tests as needed, e.g., test_depop(driver), etc.
        finally:
            driver.quit()

# Automatically run tests when the script is executed
if __name__ == "__main__":
    run_tests()
