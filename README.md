# Vendoo Automation

This repository contains a Python script to automate the process of cross-listing products on Vendoo using Selenium. The script handles various tasks such as updating product descriptions, selecting brands, adjusting conditions, updating colors, tags, categories, sizes, and measurements, verifying shipping information, and saving changes.

## Features

- **Automated Product Description Update**: Extracts and updates the product description based on predefined rules.
- **Brand Selection**: Automatically selects and adds up to three brands for the product listing.
- **Condition Update**: Sets the product's condition based on predefined criteria.
- **Color Update**: Determines the color from the description and sets it in the product listing.
- **Tag Update**: Clears existing tags and applies new tags based on the product's description.
- **Category Update**: Sets the product category according to keywords found in the description.
- **Size Update**: Automatically determines and sets the product size based on the description and category.
- **Measurement Update**: Updates measurements like waist, inseam, chest, length, and leg opening based on the description.
- **Shipping Verification**: Verifies and corrects the shipping address if necessary.
- **Automated Cross-Listing**: Runs the entire automation process from description update to shipping verification.

## Getting Started (unfinished)

### Prerequisites

- Python 3.x
- Selenium WebDriver
- A WebDriver executable (e.g., ChromeDriver)
