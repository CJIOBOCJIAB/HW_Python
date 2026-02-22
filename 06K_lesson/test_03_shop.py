import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def browser():
    # Настройка браузера FireFox
    driver = webdriver.Firefox()
    driver.set_window_size(1900, 1000)
    yield driver
    driver.quit()


@pytest.mark.usefixtures("browser")
class TestBuyShop:

    def test_buy(self, browser):
        # Настройка ожиданий
        browser.implicitly_wait(10)
        wait = WebDriverWait(browser, 10, 0.1)
        # Откройте сайт магазина: https://www.saucedemo.com/
        browser.get("https://www.saucedemo.com/")

        # Авторизуйтесь как пользователь standard_user
        input_u_n = browser.find_element(
            By.CSS_SELECTOR, '[name="user-name"]')
        input_u_n.send_keys('standard_user')

        input_pas = browser.find_element(
            By.CSS_SELECTOR, '[name="password"]')
        input_pas.send_keys('secret_sauce')

        login_button = browser.find_element(
            By.CSS_SELECTOR, '[name="login-button"]')
        login_button.click()
        print("Переход к товарам")

        # Добавьте в корзину товары:
        # Sauce Labs Backpack
        add_backpack = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '[id="add-to-cart-sauce-labs-backpack"]')))
        add_backpack.click()
        print("Backpack : добавлено")
        # Sauce Labs Bolt T-Shirt
        add_bolt = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '[id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        add_bolt.click()
        print("Bolt : добавлено")
        # Sauce Labs Onesie
        add_onesie = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '[id="add-to-cart-sauce-labs-onesie"]')))
        add_onesie.click()
        print("Onesie : добавлено")

        # Перейдите в корзину.
        basket = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.shopping_cart_link')))
        basket.click()
        print("Переход в корзину")

        # Нажмите Checkout
        checkout = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="checkout"]')))
        checkout.click()
        print("Переход к заполнению данных")

        # Заполните форму своими данными:
        # имя
        input_first_name = browser.find_element(
            By.CSS_SELECTOR, '[name="firstName"]')
        input_first_name.send_keys('Илья')
        # фамилия
        input_last_name = browser.find_element(
            By.CSS_SELECTOR, '[name="lastName"]')
        input_last_name.send_keys('CJIOBOCJIAB')
        # почтовый индекс
        input_zip_code = browser.find_element(
            By.CSS_SELECTOR, '[name="postalCode"]')
        input_zip_code.send_keys('1234567890')

        # Нажмите кнопку Continue
        input_continue = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[name="continue"]')))
        input_continue.click()
        print("Переход к (Total)")

        # Прочитайте со страницы итоговую стоимость (Total)
        try:
            total_element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '[data-test="total-label"]')))
            result = total_element.get_attribute("textContent").strip()

            # Ищем сумму в формате $XX.XX
            sum_match = re.search(r'\$(\d+\.\d{2})', result)
            if not sum_match:
                raise AssertionError(
                    f"Не удалось извлечь сумму из текста: '{result}'")

            actual_total = float(sum_match.group(1))
            expected_total = 58.29

            assert actual_total == expected_total, (
                f"Итоговая сумма не равна ${expected_total}\n"
                f"Ожидалось: ${expected_total}\n"
                f"Получено:   ${actual_total}\n"
            )

            print("Тест пройден: результат $58.29")
        except NoSuchElementException:
            assert False, "Элемент с итоговой суммой не найден на странице"
