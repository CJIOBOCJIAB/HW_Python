from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.saucedemo.com/")

    def params(self, username, password):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="user-name"]').send_keys(username)
        print("\nПользователь:", username)

        self.driver.find_element(
            By.CSS_SELECTOR, '[name="password"]').send_keys(password)
        print("Пароль : ", password)

    def login(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="login-button"]').click()
        print('Переход к "Products"')
