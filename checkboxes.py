import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver_path = 'D:\\automation\\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/")

buttons=driver.find_element(By.XPATH,'//a[@href="/checkboxes"]')
buttons.click()
checkboxes=driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
# Check the first checkbox if it is unchecked
# Check the first checkbox if it is unchecked
if checkboxes[0].is_selected():
    print("Checkbox 1 is already checked.")
else:
    checkboxes[0].click()
    print("Checkbox 1 has been checked.")

# Uncheck the second checkbox if it is checked
if checkboxes[1].is_selected():
    checkboxes[1].click()
    print("Checkbox 2 has been unchecked.")
else:
    print("Checkbox 2 is already unchecked.")

time.sleep(10)
driver.quit()