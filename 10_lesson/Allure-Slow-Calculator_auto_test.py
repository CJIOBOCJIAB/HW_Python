import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.CalculatorPage import SlowCalculator


@pytest.fixture
def browser():
    """
    Фикстура PyTest для настройки и очистки окружения браузера.

    Создаёт и настраивает экземпляр драйвера Chrome,
    устанавливает размер окна,
    передаёт драйвер в тестовую функцию,
    а после завершения теста закрывает браузер.

    Returns:
        webdriver.Chrome: инициализированный
        и настроенный экземпляр драйвера Chrome.
    """
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(1900, 1000)
    yield driver
    driver.quit()


@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения чисел в калькуляторе с задержкой 45 секунд")
@allure.description(
    "Тест проверяет корректность выполнения операции сложения "
    "в калькуляторе с установленной задержкой в 45 секунд. "
    "Сценарий: 7 + 8 = 15"
)
def test_slow_calculator(browser):
    """
    Тест, проверяющий работу калькулятора с задержкой.

    Args:
        browser (webdriver.Chrome): фикстура,
        предоставляющая экземпляр драйвера браузера.
    """
    sc = SlowCalculator(browser)

    with allure.step("Установка задержки в 45 секунд"):
        sc.delay('45')

    with allure.step("Ввод первого числа: 7"):
        sc.press_num('7')

    with allure.step("Нажатие оператора сложения"):
        sc.press_operator('+')

    with allure.step("Ввод второго числа: 8"):
        sc.press_num('8')

    with allure.step("Нажатие кнопки равно"):
        sc.press_equal()

    with allure.step("Получение результата с экрана калькулятора"):
        result = sc.screen('15')

    with allure.step(
            f"Проверка результата:"
            f"ожидаемое значение '15', фактическое — '{result}'"):
        to_be = '15'
        assert result == to_be, (
            f"Ожидаемый результат {to_be},"
            f"но получен {result}")
