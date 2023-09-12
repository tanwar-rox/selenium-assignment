# Import necessary libraries
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Initialize the WebDriver (in this case, we'll use Chrome)
driver = webdriver.Chrome()

# Navigate to the web application login page (We are using LinkedIn here)
driver.get("https://www.linkedin.com/home")

# Find the username and password input fields by their HTML attributes (e.g., name, id, or XPath)

user_name_input = driver.find_element(By.ID, "session_key")# Replace with the actual ID or attribute of the username field
password_input = driver.find_element(By.ID, "session_password")# Replace with the actual ID or attribute of the password field

# Enter your login credentials (replace 'your_username' and 'your_password' with actual credentials)
user_name_input.send_keys("vishaltanwar699@gmail.com")
password_input.send_keys("Tanwar@2001")


# Submit the login form (this may require finding the login button and clicking it)
login_button = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width") # Replace with the actual ID or attribute of the login button

login_button.click()

# Waiting time 10s
time.sleep(10)

# Optionally, you can add a wait statement to ensure the login is successful
# (e.g., wait for a specific element on the dashboard after successful login)

# Close the WebDriver after the test is complete
driver.quit()



