from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()


driver.get("https://www.linkedin.com/home")


user_name_input = driver.find_element(By.ID, "session_key")
password_input = driver.find_element(By.ID, "session_password")

user_name_input.send_keys("vishaltanwar699@gmail.com")
password_input.send_keys("")

login_button = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width")

login_button.click()

time.sleep(10)

driver.quit()



