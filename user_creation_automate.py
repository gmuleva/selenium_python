from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Initialize Chrome driver with options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the login page
    driver.get("http://localhost:3000/login")

    # Input email and password
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("gourav@hph.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("welcome")

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]")
    login_button.click()

    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
    admin_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/admin']")))

    admin_button.click()

    wait = WebDriverWait(driver, 10)
    aai_mata_mandir_siwai = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'aai mata mandir siwai')]")))
    aai_mata_mandir_siwai.click()

    register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Register')]")))
    register_button.click()

    file_input = driver.find_element(By.XPATH, "//input[@id='photo']")
    file_input.send_keys('/Users/admin/Pictures/Photo Booth Library/Pictures/Photo on 19-01-21 at 8.46 AM.jpg')

    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys('asdfhgf')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='father']").send_keys('Muleva')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@value='male']").click()
    time.sleep(3)
    gotra_dropdown = driver.find_element(By.XPATH, "//input[@id='gotra']")
    gotra_dropdown.click()

    # Set gotra value directly
    gotra_dropdown.send_keys("Muleva")
    gotra_dropdown.send_keys(Keys.ENTER)

    time.sleep(3)

    mobile_no = driver.find_element(By.XPATH, '//input[@id="mobile"]')
    mobile_no.send_keys("6265719745")

    time.sleep(3)

    dob = driver.find_element(By.XPATH, '//input[@id="dob"]')
    dob.send_keys("2003-10-05")
    dob.send_keys(Keys.TAB)  # Ensure the date input is confirmed

    time.sleep(3)
    marital_status = driver.find_element(By.XPATH, '//input[@id="marital"]')
    marital_status.send_keys('Married')
    marital_status.send_keys(Keys.ENTER)

    submit_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    submit_button.click()

    # Wait for the presence of "user" on the screen after submitting the form
    try:
        user_present = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'asdfhgf')]"))
        )
        if user_present:
            print("User Created Successfully.")
    except:
        print("Test Case Failed: User Not Created")

finally:
    # Close the driver
    driver.quit()
