from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



service = Service(executable_path='D:\\driver\\chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[1]/a').click()
text=driver.find_element(By.XPATH,'//*[@id="content"]/div/p').text
print(text)

