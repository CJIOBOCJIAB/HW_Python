 # Упражнение 1. Клик по кнопке с CSS-классом
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

 # Открыть браузер Google Chrome.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
sleep(1)
driver.maximize_window()
sleep(2)

 # Перейти на страницу: http://uitestingplayground.com/classattr.
driver.get("http://uitestingplayground.com/classattr")
sleep(2)

 # Кликнуть на синюю кнопку.
search_input = driver.find_element(By.CSS_SELECTOR, '.btn-primary')

search_input.click()
sleep(5)
