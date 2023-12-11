#test case-
# 1-open chrome
# 2-open url(https://the-internet.herokuapp.com/)
# 3-perform add remove eelment
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver_path = 'D:\\automation\\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/")
element = driver.find_element(By.XPATH, '//a[@href="/add_remove_elements/"]')
element.click()
for i in range(5):
    add_element = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    add_element.click()

for a in range(5):
    remove_element = driver.find_element(By.XPATH,'//button[@onclick="deleteElement()"]')
    remove_element.click()
time.sleep(10)
driver.quit()