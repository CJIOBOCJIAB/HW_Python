from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Product:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)

    def add_to_cart(self, product):

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

    def go_to_cart(self):

        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()
        print('Переход к "Your Cart"')
