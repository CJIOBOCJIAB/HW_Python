 # Упражнение 4. Форма авторизации
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

 # Открыть браузер FireFox.
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
sleep(1)
driver.maximize_window()
sleep(3)

 # Перейти на страницу http://the-internet.herokuapp.com/login.
driver.get("http://the-internet.herokuapp.com/login")
sleep(3)

 # В поле username ввести значение tomsmith.
search_input = driver.find_element(By.ID, "username")

search_input.send_keys("tomsmith")
sleep(3)

 # В поле password ввести значение SuperSecretPassword!.
search_input = driver.find_element(By.ID, "password")

search_input.send_keys("SuperSecretPassword!")
sleep(3)

 # Нажать кнопку Login.
search_input = driver.find_element(By.CSS_SELECTOR, "button.radius")

search_input.click()
sleep(3)

 # Вывести текст с зеленой плашки в консоль.
search_input = driver.find_element(By.ID, "flash")

text = search_input.get_attribute("textContent").strip()
print(text[:-1])

 # Закрыть браузер (метод quit()).
driver.quit()