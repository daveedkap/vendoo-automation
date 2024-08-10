# test_main_script.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from main import automate_crosslisting

driver = webdriver.Chrome()

# Log in
driver.get("https://web.vendoo.co/login")
time.sleep(1)

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

username_field.send_keys("dkaplanskybrimmer@gmail.com")
password_field.send_keys("passwordfortesting")

login_button = driver.find_element(By.ID, "login-btn")
login_button.click()
time.sleep(1)

# Navigate to the specific item
driver.get("https://web.vendoo.co/app/item/Xl6YXpLpyavswcXdrW2m?marketplace=grailed")
time.sleep(1)

# Call main
automate_crosslisting(driver)

# Close the browser after the test
driver.quit()