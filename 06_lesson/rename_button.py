from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.set_window_size(1900, 1000)

driver.implicitly_wait(10)
driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, '[id="newButtonName"]')
element.clear()
element.send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, '[id="updatingButton"]').click()
txt = driver.find_element(By.CSS_SELECTOR, '[id="updatingButton"]').text
print(f'"{txt}"')

driver.quit()
