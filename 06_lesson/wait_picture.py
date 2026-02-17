from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.set_window_size(1900, 1000)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 20)
waiter.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '[id="text"]'), "Done!"))

imgs = driver.find_elements(By.CSS_SELECTOR, 'img')
print(imgs[2].get_attribute("src"))

driver.quit()
