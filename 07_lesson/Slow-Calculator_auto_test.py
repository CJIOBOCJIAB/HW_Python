import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.CalculatorPage import SlowCalculator


@pytest.fixture
def browser():
    # Настройка браузера Google Chrome
    service = ChromeService(
        ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(1900, 1000)
    yield driver
    driver.quit()


def test_slow_calculator(browser):

    sc = SlowCalculator(browser)

    sc.delay('45')

    sc.press_num('7')
    sc.press_operator('+')
    sc.press_num('8')
    sc.press_equal()

    result = sc.screen('15')
    to_be = '15'
    # модули уникальных значений
    # sc.press_clear()
    # ('x')
    # ('÷')
    # ('.')
    assert result == to_be
