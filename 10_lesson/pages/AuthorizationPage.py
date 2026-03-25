import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Authorization:
    """
    Класс представляет собой абстракцию страницы
    авторизации для автоматизации тестирования.
    Обеспечивает взаимодействие с элементами
    интерфейса авторизации через Selenium WebDriver.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует экземпляр класса, настраивает
        WebDriver и открывает страницу авторизации.

        Args:
            driver (webdriver.Firefox):экземпляр драйвера браузера Firefox.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод учётных данных: пользователь {username}")
    def params(self, username: str, password: str) -> None:
        """
        Вводит учётные данные пользователя в поля авторизации.

        Args:
            username (str): имя пользователя для авторизации.
            password (str): пароль пользователя для авторизации.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="user-name"]').send_keys(username)
        print("\nПользователь:", username)

        self.driver.find_element(
            By.CSS_SELECTOR, '[name="password"]').send_keys(password)
        print("Пароль : ", password)

    @allure.step("Нажатие кнопки авторизации")
    def login(self) -> None:
        """
        Нажимает кнопку авторизации для перехода на страницу товаров.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="login-button"]').click()
        print('Переход к "Products"')
