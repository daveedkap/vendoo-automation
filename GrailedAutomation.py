from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Make field retrieval consistent. For example: by.ID / CSS selector
class GrailedAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.new_description = "" 
        self.colors = ["Beige", "Black", "Blue", "Brown", "Cream", "Gold", "Gray", "Green",
                        "Multicolor", "Orange", "Pink", "Purple", "Red", "Silver", "Yellow", "Tan", "White"]
        self.denim = ["Stonewash", "Darkwash", "Lightwash"]
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
            "Shorts": "Menswear > Bottoms > Shorts",
            "Jorts": "Menswear > Bottoms > Shorts",
            "Tee": "Menswear > Tops > Short Sleeve T-Shirts",
            "Hoodie": "Menswear > Tops > Sweatshirts & Hoodies",
            "Sweatshirt": "Menswear > Tops > Sweatshirts & Hoodies",
            "Crewneck": "Menswear > Tops > Sweatshirts & Hoodies",
            "Jacket": "Menswear > Outerwear > Light Jackets",
            "Beanie": "Menswear > Accessories > Hats",
            "Cap": "Menswear > Accessories > Hats",
            "Sneaker": "Menswear > Footwear > Low-Top Sneakers",
            "Boot": "Menswear > Footwear > Boots"
        }

        self.measurement_map = {
            "Jeans": {"inseam": "length (inseam): ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Workwear Pants": {"inseam": "length (inseam): ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Cargo Pants": {"inseam": "length (inseam): ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Sweatpants": {"inseam": "length (inseam): ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Track Pants": {"inseam": "length (inseam): ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Ski Pants": {"inseam": "length (inseam): ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Cargo Shorts": {"inseam": "inseam: ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Jorts": {"inseam": "inseam: ", "waist": "waist: ", "leg opening": "leg opening: "},
            "Tee": {"chest": "width (pit-to-pit): ", "length": "length: "},
            "Hoodie": {"chest": "width (pit-to-pit): ", "length": "length: "},
            "Jacket": {"chest": "width (pit-to-pit): ", "length": "length: "}
        }

        self.measurement_fields = {
            "waist": "listings.grailed.marketplaceSpecifics.measurements.waist",
            "inseam": "listings.grailed.marketplaceSpecifics.measurements.inseam",
            "leg opening": "listings.grailed.marketplaceSpecifics.measurements.leg_opening",
            "chest": "listings.grailed.marketplaceSpecifics.measurements.chest",
            "length": "listings.grailed.marketplaceSpecifics.measurements.length"
        }

        self.tags_map = { #needs work due to a certain issue: what if we get CRAZY tommy jeans? or rocawear sweats? etc. handle these.
            # think about creating a specific ID for each description's category. map THOSE id's to the tags instead. 
            "tommy hilfiger": "#streetwear #workwear #vintage #y2k #levis #carhartt #dickies #jnco #harleydavidson #tommyhilfiger",
            "tee": "#streetwear #workwear #vintage #y2k #levis #carhartt #dickies #jnco #harleydavidson #tommyhilfiger",
            "hoodie": "#streetwear #workwear #vintage #y2k #levis #carhartt #dickies #jnco #harleydavidson #tommyhilfiger",
            "jacket": "#streetwear #workwear #vintage #y2k #levis #carhartt #dickies #jnco #harleydavidson #tommyhilfiger",
            "nike": "#streetwear #sportswear #vintage #y2k #adidas #nike #reebok #champion #russellathletic #newbalance",
            "bootcut": "#streetwear #vintage #y2k #jnco #missme #affliction #silver #edhardy #juicycouture #truereligion",
            "rocawear": "#streetwear #vintage #y2k #jnco #rocawear #eckounltd #southpole #coogi #pepe #truereligion",
            "ski": "#streetwear #vintage #y2k #jnco #patagonia #thenorthface #arcteryx #columbia #goretex #burton",
            "beanie": "#streetwear #vintage #y2k #skater #grunge #jnco #workwear #truereligion #arcteryx #carhartt",
            "cap": "#streetwear #vintage #y2k #skater #grunge #jnco #workwear #truereligion #arcteryx #carhartt",
            "boot": "#streetwear #vintage #y2k #skater #grunge #nike #harleydavidson #vans #newrock #rickowens",
            "sneaker": "#streetwear #vintage #y2k #skater #grunge #nike #harleydavidson #vans #newrock #rickowens"
        }

        self.size_element_map = {
            "Jeans": "listings.grailed.categorySpecifics.bottoms.denim_size",
            "Workwear Pants": "listings.grailed.categorySpecifics.bottoms.casual_pants_size",
            "Cargo Pants": "listings.grailed.categorySpecifics.bottoms.casual_pants_size",
            "Ski Pants": "listings.grailed.categorySpecifics.bottoms.casual_pants_size",
            "Sweatpants": "listings.grailed.categorySpecifics.bottoms.sweatpants_joggers_size",
            "Track Pants": "listings.grailed.categorySpecifics.bottoms.sweatpants_joggers_size",
            "Cargo Shorts": "listings.grailed.categorySpecifics.bottoms.shorts_size",
            "Jorts": "listings.grailed.categorySpecifics.bottoms.shorts_size",
            "Shorts": "listings.grailed.categorySpecifics.bottoms.shorts_size",
            "Tee": "listings.grailed.categorySpecifics.tops.short_sleeve_shirts_size",
            "Hoodie": "listings.grailed.categorySpecifics.tops.sweatshirts_hoodies_size",
            "Sweatshirt": "listings.grailed.categorySpecifics.tops.sweatshirts_hoodies_size",
            "Crewneck": "listings.grailed.categorySpecifics.tops.sweatshirts_hoodies_size",
            "Jacket": "listings.grailed.categorySpecifics.outerwear.light_jackets_size",
            "Sneaker": "listings.grailed.categorySpecifics.footwear.lowtop_sneakers_size",
            "Boot": "listings.grailed.categorySpecifics.footwear.boots_size",
            "Beanie": "listings.grailed.categorySpecifics.accessories.hats_size"
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
            print(f"Found color: {found_color} (based on 'stonewash' or 'lightwash' or 'darkwash')")
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
        # Determine which tags to use based on the description content
        tags_to_use = ""
        for keyword, tags in self.tags_map.items():
            if keyword in self.new_description.lower():
                tags_to_use = tags
                break
        if tags_to_use:
            # Add conditional check to see if the tags box is already empty or not.
            # clear_tags_button = self.wait_for_element(By.CSS_SELECTOR, ".react-select__clear-indicator")
            # clear_tags_button.click()

            # Click into the tags section
            tags_input = self.wait_for_element(By.CSS_SELECTOR, ".react-select__input-container")
            tags_input.click()

            # Send the appropriate hashtags
            tags_input_field = self.wait_for_element(By.ID, "listings.grailed.marketplaceSpecifics.hashtags")
            for tag in tags_to_use.split():
                tags_input_field.send_keys(tag)
                tags_input_field.send_keys(Keys.ENTER)

            print(f"Tags updated: {tags_to_use}")
        else:
            print("No matching keywords found in the description.")

        time.sleep(2)

    def update_sizing(self):
        # Determine the category of the item based on the description
        selected_category = None
        for category in self.description_categories:
            if category.lower() in self.new_description.lower():
                selected_category = category
                break

        # Check if the selected category is found in the size element map
        if selected_category and selected_category in self.size_element_map:
            size_field_id = self.size_element_map[selected_category]

            # Handle "Beanie" and "Cap" categories separately
            if selected_category.lower() in ["beanie", "cap"]:
                # Directly set the size to "One Size"
                size_container = self.wait_for_element(By.XPATH, "//div[@id='react-select-17-placeholder']")
                size_container.click()
                size_input = self.wait_for_element(By.ID, size_field_id)
                self.clear_and_send_keys(size_input, "One Size")
                size_input.send_keys(Keys.ENTER)
                print(f"Size updated to: One Size")
            else:
                # Read the description and find the appropriate size value
                size_value = None
                if selected_category.lower() in ["tee", "hoodie", "sweatshirt", "crewneck", "jacket"]:
                    # Look for a letter (e.g., S, M, L, XL)
                    for line in self.new_description.lower().split('\n'):
                        if "size: " in line:
                            size_value = ''.join(char for char in line.split("size: ")[1] if char.isalpha())
                            break
                elif selected_category.lower() in ["sneaker", "boot"]:
                    # Look for a float number (do not round)
                    for line in self.new_description.lower().split('\n'):
                        if "size: " in line:
                            size_value = ''.join(char for char in line.split("size: ")[1] if char.isdigit() or char == '.')
                            break
                else:
                    # Look for a number and round to the nearest integer
                    for line in self.new_description.lower().split('\n'):
                        if "waist: " in line:  # Check the line, not the whole description
                            size_value = ''.join(char for char in line.split("waist: ")[1] if char.isdigit() or char == '.')
                            size_value = float(size_value)
                            if size_value > 40:
                                size_value = 40
                            size_value = str(round(size_value))
                            break

                # Default to "One Size" if no value is found
                if not size_value:
                    size_value = "One Size"

                # Locate the size input field's container and click into it
                size_container = self.wait_for_element(By.XPATH, f"//div[@class='react-select__control css-1s2u09g-control']//input[@id='{size_field_id}']")
                size_container.click()

                # Locate the input within the container and send the size value
                size_input = self.wait_for_element(By.ID, size_field_id)
                self.clear_and_send_keys(size_input, size_value)
                size_input.send_keys(Keys.ENTER)

                print(f"Size updated to: {size_value}")
        else:
            print("No matching category found in the description.")

        time.sleep(2)

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

            
        time.sleep(2)

    def update_measurements(self):
        # Determine the correct measurement keywords based on clothing type
        clothing_type = None
        for category in self.description_categories:
            if category.lower() in self.new_description.lower():
                clothing_type = category
                break

        # Extract and input measurements based on the determined clothing type
        if clothing_type and clothing_type in self.measurement_map:
            for key, keyword in self.measurement_map[clothing_type].items():
                if keyword.lower() in self.new_description.lower():
                    measurement_value = self.new_description.lower().split(keyword.lower())[1].split()[0]
                    field_id = self.measurement_fields[key]
                    input_element = self.wait_for_element(By.ID, field_id)
                    self.clear_and_send_keys(input_element, measurement_value)
        
        time.sleep(1)
        print(f"Measurements updated for {clothing_type}")

    def verify_shipping(self):
        # Locate the shipping address input field
        shipping_input = self.wait_for_element(By.ID, "listings.grailed.marketplaceSpecifics.shippingForm.address")
        
        # Get the current value of the shipping address
        current_address = shipping_input.get_attribute('value')
        correct_address = "David Kaplansky 71 Putnam St"
        
        # Verify if the current address is correct
        if current_address != correct_address:
            print(f"Address is incorrect. Found: {current_address}. Updating to correct address.")
            self.clear_and_send_keys(shipping_input, correct_address)
            shipping_input.send_keys(Keys.RETURN)
        else:
            print("Shipping address is correct.")

        time.sleep(1)

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
        self.update_tags()

        # Category
        self.update_category()

        # Sizing
        self.update_sizing()

        # Measurements
        self.update_measurements()

        # Verifying Shipping
        self.verify_shipping()

        # Save changes
        # self.save_changes() # We don't want to save changes yet

        time.sleep(3)
