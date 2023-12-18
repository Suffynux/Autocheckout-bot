from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# Opening the browser
driver = webdriver.Chrome()

# Head to Amazon's homepage
driver.get("https://www.amazon.com/")

# Wait for the search box to be present before interacting with it
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Perform some actions on the search box (e.g., type something)
# item = (input("Enter the item you want to search"))
search_box.send_keys("playstataion portal")

# Find and click the submit button using its XPath
submit_button_xpath = '//*[@id="nav-search-submit-button"]'
submit_button = driver.find_element(By.XPATH, submit_button_xpath)
submit_button.click()


# selecting the playstation portal 
driver.find_element(By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal").click()
# Add a sleep to keep the browser open for a while (you can replace this with your desired actions)
time.sleep(10)

# Close the browser when done
driver.quit()
