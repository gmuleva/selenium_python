# test case-
# 1-open chrome
# 2-open url(https://the-internet.herokuapp.com/)
# 3-perform broken image

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = 'D:\\automation\\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/")
element = driver.find_element(By.XPATH, '//a[@href="/broken_images"]')
element.click()

try:
    # Find all image elements on the page
    images = driver.find_element(By.TAG_NAME, "img")

    # Iterate through the images and check for broken ones
    for img in images:
        src = img.get_attribute("src")
        response = requests.head(src)

        # Check if the response status code indicates a broken image
        if response.status_code != 200:
            print(f"Broken Image: {src}")

except Exception as e:
    print(f"An error occured: {e}")

finally:

    driver.quit()


