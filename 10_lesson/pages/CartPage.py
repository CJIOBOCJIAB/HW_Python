import allure
from selenium.webdriver.common.by import By


class Cart:
    """
    Класс представляет собой абстракцию страницы
    корзины для автоматизации тестирования.
    Обеспечивает взаимодействие с элементами
    интерфейса корзины через Selenium WebDriver.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует экземпляр класса.

        Args:
            driver (webdriver.Firefox):
            экземпляр драйвера браузера Firefox.
        """
        self.driver = driver

    @allure.step("Нажатие кнопки оформления заказа")
    def checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа
        для перехода к вводу информации о доставке.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="checkout"]').click()
        print('Переход к "Your Information"')
