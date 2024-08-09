from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Initialize the WebDriver
s = Service('/Users/luccapiconroura/Desktop/DepopAutomator/chromedriver')
driver = webdriver.Chrome(service=s)

# Function to login to the website
# def login(email, password):
#     driver.get("https://web.vendoo.co/app/")
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
#     driver.find_element(By.NAME, "email").send_keys(email)
#     driver.find_element(By.NAME, "password").send_keys(password)
#     driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

# Main automation function
def automate_crosslisting():
    # login("luccadavidvintage@gmail.com", "Atheistjew123")
    
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-card")))
    # items = driver.find_elements(By.CSS_SELECTOR, ".item-card")
    
    # for item in items[:num_items_to_process]:
    #     item.click()
    
    # Wait for the Grailed button to be clickable and then click it
        # grailed_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "grailed"))
        # )
        # grailed_button.click()
        
        # Locate the description textarea and get the existing text
        description_textarea = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "listings.grailed.overrides.description"))
        )
        current_description = description_textarea.get_attribute('value')

        # Process the description to remove the first line and any extra space
        lines = current_description.split('\n')
        new_description = '\n'.join(lines[2:]).strip()

        # Clear the text area and input the modified description
        description_textarea.clear()  # Clears the textarea
        description_textarea.send_keys(new_description)  # Inputs the new description

        # Brands
        # Inputting first brand
        brand_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.brands[0]"))
        )
        brand_input.click()  # Click the input field to ensure it's active
        brand_input.clear()  # Clear any pre-filled content in the input field
        brand_input.send_keys("Vintage")  # Enter the brand name

        add_brand_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "styles__AdditionButtonStyled"))
        )
        add_brand_button.click()

        # Inputting second brand
        brand_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.brands[1]"))
        )
        brand_input.click()  # Click the input field to ensure it's active
        brand_input.clear()  # Clear any pre-filled content in the input field
        brand_input.send_keys("Jnco")  # Enter the brand name

        # add_brand_button = WebDriverWait(driver, 10).until(
        # EC.element_to_be_clickable((By.CLASS_NAME, "styles__AdditionButtonStyled"))
        # )
        add_brand_button.click()

        # Inputting third brand
        brand_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.brands[1]"))
        )
        brand_input.click()  # Click the input field to ensure it's active
        brand_input.clear()  # Clear any pre-filled content in the input field
        brand_input.send_keys("Streetwear")  # Enter the brand name

        
        # Condition
        driver.find_element(By.ID, "listings.grailed.overrides.condition-formGroupLabel").click()
        driver.find_element(By.XPATH, "//option[text()='Gently Used']").click()
        
        # Tags
        tags_input = driver.find_element(By.ID, "listings.grailed.marketplaceSpecifics.hashtags-multi-selector-container")
        tags_input.send_keys("#streetwear #workwear #vintage #y2k #levis #carhartt #dickies #jnco #lee #tommyhilfiger")
        
        # Sizing
        waist = int(description_text.split("waist: ")[1].split()[0])
        size = waist if waist < 40 else 40
        driver.find_element(By.ID, "listings.grailed.categorySpecifics.bottoms.casual_pants_size-multi-selector-container").send_keys(str(size) + Keys.ENTER)

        # Measureuments tab
        # W.I.P

        # Save
        driver.find_element(By.ID, "save-item-button").click()
        time.sleep(3)  # Wait for the item to save
        # driver.find_element(By.ID, "Back to Inventory").click() # Go back to inventory to work on next item

# num_items_to_process = 9  # Change this number as needed

# Run the automation
automate_crosslisting(1)