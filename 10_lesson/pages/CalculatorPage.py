import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculator:
    """
    Класс представляет собой абстракцию страницы
    калькулятора для автоматизации тестирования.
    Обеспечивает взаимодействие с элементами
    интерфейса калькулятора через Selenium WebDriver.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует экземпляр класса,
        настраивает WebDriver и открывает страницу калькулятора.

        Args:
            driver (webdriver.Chrome): экземпляр драйвера браузера Chrome.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.maximize_window()
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")
        self.delay_seconds = None

    @allure.step("Установка задержки калькулятора: {seconds} секунд")
    def delay(self, seconds: str | int) -> None:
        """
        Устанавливает задержку для операций калькулятора.

        Args:
            seconds (str | int): количество секунд задержки.
            Будет преобразовано в строку при отправке в поле ввода.
        """
        self.delay_seconds = seconds
        input_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'delay')))
        input_field.clear()
        input_field.send_keys(str(seconds))
        print("\nПоставлена задержка : ", seconds)

    @allure.step("Нажатие цифры: {number}")
    def press_num(self, number: str | int) -> None:
        """
        Нажимает на кнопку с цифрой на калькуляторе.

        Args:
            number (str | int): цифра, которую нужно нажать.
            Будет преобразована в строку для поиска элемента.
        """
        number_str = str(number)
        element = (f"//span["
                   f"@class='btn btn-outline-primary' and contains("
                   f"text(), '{number_str}')]"
                   )
        key_num = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, element)))
        key_num.click()
        print("Нажата кнопка : ", number)

    @allure.step("Нажатие оператора: {sign}")
    def press_operator(self, sign: str) -> None:
        """
        Нажимает на кнопку оператора (+, -, ×, ÷) на калькуляторе.

        Args:
            sign (str): оператор, который нужно нажать (например, '+', '-').
        """
        sign_str = str(sign)
        element = f"//span[text()='{sign_str}']"
        key_sign = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, element))
        )
        key_sign.click()
        print("Нажата кнопка : ", sign)

    @allure.step("Нажатие кнопки 'равно'")
    def press_equal(self) -> None:
        """
        Нажимает на кнопку «равно» (=)
        на калькуляторе для выполнения вычисления.
        """
        key_equal = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.btn.btn-outline-warning')))
        key_equal.click()
        print("Нажата кнопка : равно")

    @allure.step("Нажатие кнопки очистки экрана")
    def press_clear(self) -> None:
        """
        Нажимает на кнопку очистки экрана (C) на калькуляторе.
        """
        key_clear = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.clear.btn.btn-outline-danger')))
        key_clear.click()
        print("Нажата кнопка : очистить экран")

    @allure.step(
        "Ожидание и получение результата на экране:"
        "ожидаемое значение '{value}'")
    def screen(self, value: str | int) -> str:
        """
        Ожидает появления результата на экране калькулятора и возвращает его.

        Args:
            value (str | int): ожидаемое значение на экране.
            Будет использовано для проверки наличия текста в элементе экрана.

        Returns:
            str: текст, отображаемый на экране калькулятора
            (очищенный от лишних пробелов).
        """
        timeout = self.delay_seconds
        wait_long = WebDriverWait(self.driver, timeout, 0.5)

        element_screen = wait_long.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.screen'))
        )

        wait_long.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.screen'), str(value)))

        result = element_screen.get_attribute("textContent").strip()
        print(f"Результат на экране: {result}")
        return result
