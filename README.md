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

## Getting Started 


##For MACOS:


To get this project running on your Mac in Visual Studio Code (VSCode), you'll need to follow these steps:

### 1. **Install Python and Pip**
   - **Check Python Installation:**
     - Open your terminal and type:

       python3 --version

       If Python is not installed, follow the steps below to install it.

   - **Install Python:**
     - Go to Python's official website (https://www.python.org/downloads/) and download the latest version for macOS.
     - Follow the installation instructions.

   - **Ensure Pip is Installed:**
     - Pip is usually installed with Python. To check if Pip is installed, type:

       pip3 --version

     - If it's not installed, you can install it using:
       sudo easy_install pip

### 2. **Install VSCode**
   - Download and install Visual Studio Code from the official website (https://code.visualstudio.com/).
   - After installation, open VSCode.

### 3. **Install the Python Extension for VSCode**
   - In VSCode, go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
   - Search for "Python" and install the extension provided by Microsoft.

### 4. **Install Required Libraries**
   - Next, you need to install the necessary Python libraries using `pip`:

     pip3 install selenium

   - This will install the Selenium library

### 5. **Download and Install ChromeDriver**
   - **Determine Chrome Version:**
     - Open Chrome and go to `chrome://settings/help` to check your Chrome version.
   - **Download the Corresponding ChromeDriver:**
     - Visit the ChromeDriver download page: (https://googlechromelabs.github.io/chrome-for-testing/) and download the version that matches your Chrome browser version.
   - **Install ChromeDriver:**
     - Unzip the downloaded file and move `chromedriver` to `/usr/local/bin`:

       sudo mv chromedriver /usr/local/bin/

To start working on the project from a GitHub repository on your Mac, follow these steps:

### 1. **Clone the Repository**
   - Open Terminal on your Mac.
   - Navigate to the directory where you want to clone the project, for example:

     cd ~/Projects_Example

   - Clone the repository using the following command:

     git clone https://github.com/daveedkap/vendoo-automation.git

   - This will download the project files to your local machine.

### 2. **Navigate to the Project Directory**
   - After cloning, navigate to the project directory:

     cd ‘vendoo-automation’

### 3. **Open the Project in VSCode**
   - Open VSCode and select `File > Open...`.
   - Navigate to the project directory and open it.
   - VSCode will load the project, and you’ll see the files in the Explorer view.

### 4. **Run the Project**
   - Open the main testing Python file in VSCode (GrailedAutomationTest.py).
   - Run the script


##For Windows:


To set up and run the provided project on Windows in Visual Studio Code (VSCode), follow these steps:

### 1. **Install Python and Pip**
   - **Check Python Installation:**
     - Open Command Prompt (you can search for "cmd" in the Start menu) and type:

       python --version

       If Python is not installed, follow the steps below to install it.

   - **Install Python:**
     - Go to Python's official website (https://www.python.org/downloads/) and download the latest version for Windows.
     - Make sure to check the box that says "Add Python to PATH" during installation.
     - Follow the installation instructions.

   - **Ensure Pip is Installed:**
     - Pip is usually installed with Python. To check if Pip is installed, type:

       pip --version

     - If it's not installed, Python might not be added to your PATH. You can manually add it or reinstall Python ensuring you check the "Add Python to PATH" option.

### 2. **Install VSCode (Skip if already installed)**
   - Download and install Visual Studio Code from the official website (https://code.visualstudio.com/).
   - After installation, open VSCode.

### 3. **Install the Python Extension for VSCode**
   - In VSCode, go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
   - Search for "Python" and install the extension provided by Microsoft.

### 4. **Install Required Libraries**
   - With your virtual environment activated, install the necessary Python libraries using `pip`:

     pip install selenium

   - This will install the Selenium library.


### 5. **Download and Install ChromeDriver**
   - **Determine Chrome Version:**
     - Open Chrome and go to `chrome://settings/help` to check your Chrome version.
   - **Download the Corresponding ChromeDriver:**
     - Visit the ChromeDriver download page: (https://googlechromelabs.github.io/chrome-for-testing/) and download the version that matches your Chrome browser version.
   - **Install ChromeDriver:**
     - Unzip the downloaded file by extracting the files, and move `chromedriver.exe` to a convenient and accessible directory.
     - Add this directory to your system’s PATH:
       - Right-click on "This PC" or "My Computer" and select "Properties."
       - Click on "Advanced system settings."
       - In the System Properties window, click on the "Environment Variables" button.
       - In the Environment Variables window, under "System variables," find the `Path` variable, select it, and click "Edit."
       - Click "New" and add the path to your `chromedriver.exe` (e.g., `C:\chromedriver`).
       - Click OK to close all the windows.



To start working on the project from a GitHub repository on your PC, follow these steps:

### 1. **Clone the GitHub Repository**
   - Open the command prompt and go to the path of your directory for the project:

     cd path_to_your_directory

   - Once in the correct directory, clone the repository from GitHub by running:

     git clone https://github.com/daveedkap/vendoo-automation.git

### 2. **Navigate to the Project Directory**
   - After cloning, navigate to the project directory:

     cd ‘vendoo-automation’

### 3. **Open the Project in VSCode**
   - After cloning the repository, open the project in VSCode by navigating to the folder where the repository is located and selecting `Open Folder`.
   - VSCode will load the project, and you’ll see the files in the Explorer view.


### 4. **Run the Project**
   - Now that everything is set up, you can run GrailedAutomationTest.py
