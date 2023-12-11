#test case-
# 1-open chrome
# 2-open url(https://the-internet.herokuapp.com/)
# 3-checkboxes

import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver_path = 'D:\\automation\\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/")



driver.quit()
