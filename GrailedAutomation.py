from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GrailedAutomation:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, identifier, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, identifier)))

    def clear_and_send_keys(self, element, text):
        element.click()
        element.clear()
        element.send_keys(text)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def update_description(self):
        description_textarea = self.wait_for_element(By.ID, "listings.grailed.overrides.description")
        current_description = description_textarea.get_attribute('value')
        print(f"Current Description: {current_description}")

        lines = current_description.split('\n')
        new_description = '\n'.join(lines[2:]).strip()
        print(f"New Description: {new_description}")

        description_textarea.clear()
        description_textarea.send_keys(new_description)

    def select_brand(self, brand_name, brand_index):
        brand_input = self.wait_for_element(By.ID, f"listings.grailed.overrides.brands[{brand_index}]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.wait_for_element(By.ID, "listings.grailed.overrides.brands[0]"))                  
        self.clear_and_send_keys(brand_input, brand_name)
        time.sleep(1)

        brand_dropdown = self.wait_for_element(By.XPATH, f"//div[@data-testid='select-option' and .//span[text()='{brand_name}']]")
        ActionChains(self.driver).move_to_element(brand_dropdown).click().perform()

        if brand_index < 2:
            add_brand_button = self.wait_for_element(By.CSS_SELECTOR, ".styles__AdditionButtonStyled-sc-1bqfbui-0.kGNZZf")
            add_brand_button.click()

    def update_condition(self):
        condition_input = self.wait_for_element(By.ID, "listings.grailed.overrides.condition")
        condition_input.click()

        condition_dropdown = self.wait_for_element(By.XPATH, "//div[@data-testid='select-option' and .//span[text()='Gently Used']]")
        condition_dropdown.click()
        time.sleep(5)

    def update_tags(self):
        tags_input = self.driver.find_element(By.ID, "listings.grailed.marketplaceSpecifics.hashtags-multi-selector-container")
        tags_input.send_keys("#streetwear #workwear #vintage #y2k #levis #carhartt #dickies #jnco #lee #tommyhilfiger")

    def update_sizing(self, current_description):
        waist = int(current_description.split("waist: ")[1].split()[0])
        size = waist if waist < 40 else 40
        sizing_input = self.driver.find_element(By.ID, "listings.grailed.categorySpecifics.bottoms.casual_pants_size-multi-selector-container")
        sizing_input.send_keys(str(size) + Keys.ENTER)

    def save_changes(self):
        save_button = self.wait_for_element(By.ID, "save-item-button")
        self.scroll_into_view(save_button)
        # save_button.click()

    def automate_crosslisting(self):
        self.update_description()

        # Brands
        self.select_brand("Vintage", 0)
        self.select_brand("Jnco", 1)
        self.select_brand("Streetwear", 2)

        # Condition
        self.update_condition()

        # Tags
        self.update_tags()

        # Sizing
        description_textarea = self.wait_for_element(By.ID, "listings.grailed.overrides.description")
        current_description = description_textarea.get_attribute('value')
        self.update_sizing(current_description)

        # Save changes
        self.save_changes()

        time.sleep(3)
