import re
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Description:
    """
    Класс представляет собой абстракцию страницы
    подтверждения заказа для автоматизации тестирования.
    Обеспечивает получение итоговой суммы заказа через Selenium WebDriver.
    """
    def __init__(self, driver) -> None:
        """
        Инициализирует экземпляр класса и настраивает ожидание элементов.

        Args:
            driver (webdriver.Firefox): экземпляр драйвера браузера Firefox.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)
        self.actual_total = None

    @allure.step("Получение и парсинг итоговой суммы заказа")
    def total(self) -> float:
        """
        Ожидает появления элемента с итоговой суммой,
        парсит значение и возвращает его.

        Returns:
            float: итоговая сумма заказа.
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-test="total-label"]')))
        result = total_element.get_attribute("textContent").strip()

        sum_match = re.search(r'\$(\d+\.\d{2})', result)
        actual_total = float(sum_match.group(1))
        print(f"Итоговая сумма : {actual_total}")
        return actual_total
