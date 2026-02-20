import pytest
import ast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    # Настройка браузера Edge
    options = webdriver.EdgeOptions()
    options.add_argument("--log-level=3")  # Только критические ошибки
    options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])  # Убрать DevTools-логи

    driver = webdriver.Edge(options=options)
    driver.set_window_size(1900, 1000)
    yield driver
    return driver


@pytest.mark.usefixtures("browser")
class TestFormValidation:

    def test_form_validation(self, browser):
        # Настройка ожиданий
        browser.implicitly_wait(10)
        # Откройте страницу: в Edge
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        # Заполните форму значениями:
        browser.find_element(
            By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
        browser.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
        browser.find_element(
            By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
        browser.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
        browser.find_element(
            By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
        # Zip code оставляем пустым
        browser.find_element(
            By.CSS_SELECTOR, '[name="zip-code"]').clear()  # явно очищаем
        browser.find_element(
            By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
        browser.find_element(
            By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
        browser.find_element(
            By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
        browser.find_element(
            By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
        # Нажмите кнопку Submit
        submit_button = browser.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        WebDriverWait(browser, 10, 0.05)
        ids = browser.find_elements(By.CSS_SELECTOR, '[id]')
        for element in ids:
            print(element.text)
        # Проверьте (assert), что поле Zip code подсвечено красным
        self.check_zip_code_element_color(ids)
        # Проверьте (assert), что остальные поля подсвечены зеленым
        self.check_all_elements_color(ids)

    @staticmethod
    def check_zip_code_element_color(ids):
        red = (132, 32, 41, 1)
        green = (15, 81, 50, 1)

        zip_code = ids[3]
        element_id = zip_code.get_attribute("id") or "без ID"
        color = zip_code.value_of_css_property("color")
        actual_rgba = ast.literal_eval(color.replace(
            "rgba", "").strip(" ()"))

        assert actual_rgba in [red, green], \
            (f"Цвет элемента {element_id} ("
             f"{actual_rgba}) не соответствует ни красному, ни зелёному")
        if actual_rgba == green:
            print(f"Элемент {element_id} — цвет поля зелёный")
        elif actual_rgba == red:
            print(f"Элемент {element_id} — цвет поля красный")

    @staticmethod
    def check_all_elements_color(ids):
        red = (132, 32, 41, 1)
        green = (15, 81, 50, 1)

        for index, element in enumerate(ids):
            if index == 3:
                continue
            else:
                element_id = element.get_attribute(
                    "id") or f"элемент_{index}"
                color = element.value_of_css_property("color")
                actual_rgba = ast.literal_eval(color.replace(
                    "rgba", "").strip(" ()"))

                assert actual_rgba in [red, green], \
                    (f"Цвет элемента {element_id} ("
                     f"{actual_rgba}"
                     f") не соответствует ни красному, ни зелёному")
                if actual_rgba == green:
                    print(f"Элемент {element_id} — цвет поля зелёный")
                elif actual_rgba == red:
                    print(f"Элемент {element_id} — цвет поля красный")
