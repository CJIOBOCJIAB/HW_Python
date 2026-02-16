from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.set_window_size(1900, 1000)

driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(f'"{txt}"')

driver.quit()
