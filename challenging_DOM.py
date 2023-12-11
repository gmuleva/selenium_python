#test case-
# 1-open chrome
# 2-open url(https://the-internet.herokuapp.com/)
# 3-perform challenging DOM
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver_path = 'D:\\automation\\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/")
element = driver.find_element(By.XPATH,'//a[@href="/challenging_dom"]')
element.click()
buttons=driver.find_element(By.XPATH,'//a[@class="button"]')
buttons.click()

# Find the element with the 'canvas' tag
canvas = driver.find_element(By.TAG_NAME,"canvas")

# Get the text attribute from the element with the 'canvas' tag
canvas_text = canvas.get_attribute("textContent")

# Print the text from the canvas
print("Text from the canvas:", canvas_text)

time.sleep(10)
driver.quit()

