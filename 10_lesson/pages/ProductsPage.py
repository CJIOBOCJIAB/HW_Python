import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Product:
    """
    Класс представляет собой абстракцию страницы
    товаров для автоматизации тестирования.
    Обеспечивает взаимодействие с элементами
    интерфейса товаров через Selenium WebDriver.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует экземпляр класса и настраивает ожидание элементов.

        Args:
            driver (webdriver.Firefox): экземпляр драйвера браузера Firefox.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)

    @allure.step("Добавление товара в корзину: {product}")
    def add_to_cart(self, product: str) -> None:
        """
        Добавляет указанный товар в корзину.

        Args:
            product (str): название товара для добавления в корзину.
        """
        product_list = {
            'Sauce Labs Backpack':
                'add-to-cart-sauce-labs-backpack',
            'Sauce Labs Bolt T-Shirt':
                'add-to-cart-sauce-labs-bolt-t-shirt',
            'Sauce Labs Onesie':
                'add-to-cart-sauce-labs-onesie',
            'Sauce Labs Bike Light':
                'add-to-cart-sauce-labs-bike-light',
            'Sauce Labs Fleece Jacket':
                'add-to-cart-sauce-labs-fleece-jacket',
            'Test.allTheThings() T-Shirt (Red)':
                'add-to-cart-test.allthethings()-t-shirt-(red)'
        }

        if product in product_list:
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, product_list[product]))).click()
            print(f'Товар : {product} добавлен в корзину')
        else:
            print(f'Товар : {product} не найден')

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины через иконку корзины в верхнем углу.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()
        print('Переход к "Your Cart"')
