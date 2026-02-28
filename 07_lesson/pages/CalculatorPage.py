from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculator:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.maximize_window()
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")
        self.delay_seconds = None

    def delay(self, seconds):
        self.delay_seconds = seconds
        input_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, 'delay')))
        input_field.clear()
        input_field.send_keys(str(seconds))
        print("\nПоставлена задержка : ", seconds)

    def press_num(self, number):

        number_str = str(number)
        element = (f"//span["
                   f"@class='btn btn-outline-primary' and contains("
                   f"text(), '{number_str}')]")
        key_num = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, element)))
        key_num.click()
        print("Нажата кнопка : ", number)

    def press_operator(self, sign):

        sign_str = str(sign)
        element = f"//span[text()='{sign_str}']"
        key_sign = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, element))
        )
        key_sign.click()
        print("Нажата кнопка : ", sign)

    def press_equal(self):
        key_equal = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '.btn.btn-outline-warning')))
        key_equal.click()
        print("Нажата кнопка : равно")

    def press_clear(self):
        key_clear = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '.clear.btn.btn-outline-danger')))
        key_clear.click()
        print("Нажата кнопка : очистить экран")

    def screen(self, value):
        timeout = self.delay_seconds
        wait_long = WebDriverWait(self.driver, timeout, 0.5)

        # Сначала находим элемент экрана (один раз)
        element_screen = wait_long.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.screen'))
        )

        # Ждём, пока в элементе появится любой текст (не пустой)
        wait_long.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.screen'), str(value)))

        result = element_screen.get_attribute("textContent").strip()
        print(f"Результат на экране: {result}")
        return result
