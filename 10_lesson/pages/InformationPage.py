import allure
from selenium.webdriver.common.by import By


class Info:
    """
    Класс представляет собой абстракцию страницы ввода
    информации о доставке для автоматизации тестирования.
    Обеспечивает взаимодействие с элементами интерфейса
    ввода информации через Selenium WebDriver.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует экземпляр класса.

        Args:
            driver (webdriver.Firefox): экземпляр драйвера браузера Firefox.
        """
        self.driver = driver

    @allure.step("Заполнение информации о доставке:"
                 "{first_name} {last_name}, индекс {zip_code}")
    def address(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполняет поля информации о доставке.

        Args:
            first_name (str): имя покупателя.
            last_name (str): фамилия покупателя.
            zip_code (str): почтовый индекс покупателя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="firstName"]').send_keys(first_name)
        print("Пользователь : ", first_name)

        self.driver.find_element(
            By.CSS_SELECTOR, '[name="lastName"]').send_keys(last_name)
        print("Пользователь : ", last_name)

        self.driver.find_element(
            By.CSS_SELECTOR, '[name="postalCode"]').send_keys(zip_code)
        print("Индекс : ", zip_code)

    @allure.step("Нажатие кнопки продолжения оформления заказа")
    def cont(self) -> None:
        """
        Нажимает кнопку продолжения для перехода
        к странице подтверждения заказа.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="continue"]').click()
        print('Переход к "Overview"')
