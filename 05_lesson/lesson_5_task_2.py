 # Упражнение 2. Клик по кнопке без ID
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

 # Открыть браузер Google Chrome.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
sleep(1)
driver.maximize_window()
sleep(3)

 # Перейти на страницу: http://uitestingplayground.com/dynamicid.
driver.get("http://uitestingplayground.com/dynamicid")
sleep(3)

 # Кликнуть на синюю кнопку.
search_input = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')

search_input.click()
sleep(5)
