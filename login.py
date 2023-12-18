
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Opening the browser
driver = webdriver.Chrome()

# Head to Amazon's homepage
driver.get("https://www.amazon.com/")

# Find and click the "Sign in" link 

sign_in_link = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
sign_in_link.click()

# Finding the email/phone number input field and enter your username
email_field = driver.find_element(By.ID, "ap_email")

# Taking the email/phone number input field

email_field.send_keys(input("Enter your.re email"))   

# Finding and click the "Continue" button

continue_button = driver.find_element(By.ID, "continue")

continue_button.click()

# Finding the password input field and enter your password
password_field = driver.find_element(By.ID, "ap_password")
password_field.send_keys(int(input("Enter your're password")))  # Replace with your actual password

# Finding and click the "Sign-In" button
sign_in_button = driver.find_element(By.ID, "signInSubmit")
sign_in_button.click()

# Add a sleep to keep the browser open for a while (you can replace this with your desired actions)
time.sleep(10)

# Close the browser when done
driver.quit()
