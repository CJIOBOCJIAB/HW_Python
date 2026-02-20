import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def browser():
    # Настройка браузера Google Chrome
    driver = webdriver.Chrome()
    driver.set_window_size(1900, 1000)
    yield driver
    driver.quit()


@pytest.mark.usefixtures("browser")
class TestSlowCalculator:

    def test_calculator(self, browser):
        # Настройка ожиданий
        browser.implicitly_wait(20)
        wait = WebDriverWait(browser, 45)
        # Откройте страницу: в Google Chrome
        browser.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/"
            "slow-calculator.html")
        # В поле ввода по локатору #delay введите значение 45.
        input_field = wait.until(
            EC.visibility_of_element_located((By.ID, 'delay')))
        input_field.clear()
        input_field.send_keys('45')

        value = input_field.get_attribute("value")
        print(f"Поле ввода содержит: {value}")

        # Нажмите на кнопки: 7 , + , 8 , =
        key_7 = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='btn btn-outline-primary'"
                           "and contains(text(), '7')]")))
        key_7.click()
        print("Нажата кнопка : ", key_7.text)

        key_sum = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='+']")))
        key_sum.click()
        print("Нажата кнопка : ", key_sum.text)

        key_8 = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='btn btn-outline-primary' "
                           "and contains(text(), '8')]")))
        key_8.click()
        print("Нажата кнопка : ", key_8.text)

        key_equal = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='=']")))
        key_equal.click()
        print("Нажата кнопка : ", key_equal.text)

        # Проверьте (assert), что результат (15 через 45 секунд)
        try:
            wait.until(
                EC.text_to_be_present_in_element((
                    By.CSS_SELECTOR, '[class="screen"]'), "15"))
            element_screen = browser.find_element(
                By.CSS_SELECTOR, '[class="screen"]')
            result = element_screen.get_attribute("textContent").strip()
            print(f"Результат на экране: '{result}'")

            # Assert с подробным сообщением
            assert result == "15", (
                f"\n Тест не пройден! Ошибка калькулятора:\n"
                f"   Ожидалось: '15'\n"
                f"   Получено:   '{result}'\n"
                f"   Задержка:   {value} с\n"
                f"   Выражение: 7 + 8 = ?"
            )
            print("Тест пройден: результат отобразился за 45 секунд")
        except TimeoutException:
            assert False, "Таймаут: результат не отобразился за 45 секунд"
