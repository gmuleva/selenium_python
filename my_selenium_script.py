from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver_path = 'D:\\automation\\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

url = 'https://www.google.com'
driver.get(url)

driver.implicitly_wait(5)

driver.quit()
