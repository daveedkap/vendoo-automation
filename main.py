from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Main automation function
def automate_crosslisting(driver):
        # Locate the description textarea and get the existing text
        description_textarea = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "listings.grailed.overrides.description"))
        )
        current_description = description_textarea.get_attribute('value')

        print(f"Current Description: {current_description}")

        lines = current_description.split('\n')
        new_description = '\n'.join(lines[2:]).strip()
        print(f"New Description: {new_description}")


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.description")))
        description_textarea.clear()  
        description_textarea.send_keys(new_description) 

        # Brands
        # Inputting first brand
        brand_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.brands[0]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", brand_input)

        brand_input.click()  # Click the input field to ensure it's active
        brand_input.clear()  # Clear any pre-filled content in the input field
        brand_input.send_keys("Vintage")  # Enter the brand name
        
        dropdown_item1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "downshift-1-item-0")))
        ActionChains(driver).move_to_element(dropdown_item1).click().perform()
    
        #error somewhere here
        add_brand_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles__AdditionButtonStyled-sc-1bqfbui-0.kGNZZf"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", add_brand_button)
        add_brand_button.click()


        # Inputting second brand
        brand_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.brands[1]"))
        )
        brand_input.click()  # Click the input field to ensure it's active
        brand_input.clear()
        brand_input.send_keys("Jnco")  # Enter the brand name
        time.sleep(1)
        brand_input.send_keys(Keys.RETURN)
        add_brand_button.click()

        # Inputting third brand
        brand_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.brands[2]"))
        )
        brand_input.click()  # Click the input field to ensure it's active
        brand_input.clear()  # Clear any pre-filled content in the input field
        brand_input.send_keys("Streetwear")  # Enter the brand name
        time.sleep(1)
        brand_input.send_keys(Keys.RETURN)


        # Condition
        condition_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "listings.grailed.overrides.condition-formGroupLabel"))
        )
        driver.find_element(By.XPATH, "//option[text()='Gently Used']").click()
        
        # Tags
        tags_input = driver.find_element(By.ID, "listings.grailed.marketplaceSpecifics.hashtags-multi-selector-container")
        tags_input.send_keys("#streetwear #workwear #vintage #y2k #levis #carhartt #dickies #jnco #lee #tommyhilfiger")
        
        # Sizing
        waist = int(current_description.split("waist: ")[1].split()[0])
        size = waist if waist < 40 else 40
        driver.find_element(By.ID, "listings.grailed.categorySpecifics.bottoms.casual_pants_size-multi-selector-container").send_keys(str(size) + Keys.ENTER)

        # Measureuments tab
        # W.I.P

        # Save
        driver.find_element(By.ID, "save-item-button").click()
        time.sleep(3)
        