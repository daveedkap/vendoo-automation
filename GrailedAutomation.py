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
        self.new_description = "" 
        self.colors = ["Beige", "Black", "Blue", "Brown", "Cream", "Gold", "Gray", "Green",
                        "Multicolor", "Orange", "Pink", "Purple", "Red", "Silver", "Yellow", "Tan", "White"]
        self.denim = ["Jeans", "Jorts"]
        self.description_categories = ["Jeans", "Workwear Pants", "Cargo Pants", "Sweatpants",
                                       "Track Pants",  "Ski Pants", "Cargo Shorts", "Jorts", "Tee",
                                        "Hoodie", "Jacket", "Beanie", "Cap",  "Sneaker", "Boot"]
        self.category_map = {
            "Jeans": "Menswear > Bottoms > Denim",
            "Workwear Pants": "Menswear > Bottoms > Casual Pants",
            "Cargo Pants": "Menswear > Bottoms > Casual Pants",
            "Ski Pants": "Menswear > Bottoms > Casual Pants",
            "Sweatpants": "Menswear > Bottoms > Sweatpants & Joggers",
            "Track Pants": "Menswear > Bottoms > Sweatpants & Joggers",
            "Cargo Shorts": "Menswear > Bottoms > Shorts",
            "Jorts": "Menswear > Bottoms > Shorts",
            "Tee": "Menswear > Tops > Short Sleeve T-Shirts",
            "Hoodie": "Menswear > Tops > Sweatshirts & Hoodies",
            "Jacket": "Menswear > Outerwear > Light Jackets",
            "Beanie": "Menswear > Accessories > Hats",
            "Cap": "Menswear > Accessories > Hats",
            "Sneaker": "Menswear > Footwear > Low-Top Sneakers",
            "Boot": "Menswear > Footwear > Boots"
        }
        
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
        self.new_description = '\n'.join(lines[2:]).strip()
        print(f"New Description: {self.new_description}")

        description_textarea.clear()
        description_textarea.send_keys(self.new_description)

    def select_brand(self, brand_name, brand_index):
        brand_input = self.wait_for_element(By.ID, f"listings.grailed.overrides.brands[{brand_index}]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.wait_for_element(By.ID, "listings.grailed.overrides.brands[0]"))                  
        self.clear_and_send_keys(brand_input, brand_name)

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

    def update_color(self):
        first_three_lines = '\n'.join(self.new_description.split('\n')[:3])
        found_color = None

        if any(denim.lower() in first_three_lines for denim in self.denim):
            found_color = "Blue"
            print(f"Found color: {found_color} (based on 'jeans' or 'jorts')")
        else:
            for color in self.colors:
                if color.lower() in first_three_lines.lower():
                    found_color = color
                    break

        if found_color:
            print(f"Found color: {found_color}")
            color_input = self.wait_for_element(By.ID, "listings.grailed.overrides.primaryColor")
            self.clear_and_send_keys(color_input, found_color)
            color_dropdown = self.wait_for_element(By.XPATH, f"//div[@data-testid='select-option' and .//strong[contains(text(), '{found_color}')]]")
            ActionChains(self.driver).move_to_element(color_dropdown).click().perform()
        else:
            print("No color found in the description.")

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
    
    def update_category(self):
        # Find which category is present in the description
        selected_category = None
        for category in self.description_categories:
            if category.lower() in self.new_description.lower():
                selected_category = category
                break

        # If a category is found, use the corresponding search keys
        if selected_category and selected_category in self.category_map:
            search_keys = self.category_map[selected_category]
            print(f"Category found: {selected_category} - Sending keys: {search_keys}")

            # Step 1: Find and click the category box
            category_box = self.wait_for_element(By.ID, "categoryV2")
            self.scroll_into_view(category_box)
            category_box.click()

            time.sleep(2)

            # Step 2: Find the search input, click, and send the appropriate keys
            category_search_input = self.wait_for_element(By.CSS_SELECTOR, "input[data-testid='category-search-field']")
            category_search_input.click()
            category_search_input.send_keys(search_keys)

            last_word = search_keys.split(" > ")[-1]
        
            # Wait for the dropdown to be populated and select the correct option
            time.sleep(2)
            category_option = self.wait_for_element(By.XPATH, f"//div[@data-testid='category-option-dropdown' and .//div[text()='{last_word}']]")
            category_option.click()

            time.sleep(2)  # Give some time for the selection to be registered
        else:
            print("No matching category found in the description.")

            
        time.sleep(15)


    def automate_crosslisting(self):
        # Description
        self.update_description()

        # Brands
        self.select_brand("Vintage", 0)
        self.select_brand("Jnco", 1)
        self.select_brand("Streetwear", 2)

        # Condition
        self.update_condition()
        
        # Color
        self.update_color()

        # Tags
        # self.update_tags()

        #Category
        self.update_category()

        # Sizing
        description_textarea = self.wait_for_element(By.ID, "listings.grailed.overrides.description")
        current_description = description_textarea.get_attribute('value')
        self.update_sizing(current_description)

        # Save changes
        # self.save_changes() # We don't want to save changes yet

        time.sleep(3)
