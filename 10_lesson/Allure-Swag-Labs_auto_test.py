import pytest
import allure
from selenium import webdriver

from pages.AuthorizationPage import Authorization
from pages.ProductsPage import Product
from pages.CartPage import Cart
from pages.InformationPage import Info
from pages.OverviewPage import Description


@pytest.fixture
def browser():
    """
    Фикстура PyTest для настройки и очистки окружения браузера Firefox.

    Создаёт и настраивает экземпляр драйвера Firefox,
    устанавливает размер окна,
    задаёт неявное ожидание, передаёт драйвер в тестовую функцию,
    а после завершения теста закрывает браузер.

    Returns:
        webdriver.Firefox: инициализированный
        и настроенный экземпляр драйвера Firefox.
    """
    driver = webdriver.Firefox()
    driver.set_window_size(1900, 1000)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature("Покупка товаров в интернет‑магазине")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title(
    "Проверка процесса покупки товаров в интернет‑магазине Sauce Demo")
@allure.description(
    "Тест проверяет полный процесс покупки: авторизацию,"
    "добавление товаров в корзину,"
    "оформление заказа и проверку итоговой суммы."
    "Сценарий: авторизация → добавление"
    "3 товаров → оформление → проверка суммы"
)
def test_buy_shop(browser):
    """
    Тест, проверяющий процесс покупки товаров в интернет‑магазине.

    Args:
        browser (webdriver.Firefox): фикстура,
        предоставляющая экземпляр драйвера браузера.
    """
    auth = Authorization(browser)
    add = Product(browser)
    cart = Cart(browser)
    info = Info(browser)
    value = Description(browser)

    with allure.step("Авторизация пользователя"):
        auth.params('standard_user', 'secret_sauce')
        auth.login()

    with allure.step("Добавление товаров в корзину"):
        add.add_to_cart('Sauce Labs Backpack')
        add.add_to_cart('Sauce Labs Bolt T-Shirt')
        add.add_to_cart('Sauce Labs Onesie')

    with allure.step("Переход в корзину"):
        add.go_to_cart()

    with allure.step("Оформление заказа"):
        cart.checkout()

    with allure.step("Заполнение информации о доставке"):
        info.address('Илья', 'Словослав', '1234567890')
        info.cont()

    with allure.step("Получение итоговой суммы"):
        actual_total = value.total()

    with ((((allure.step(
            f"Проверка итоговой суммы:"
            f"ожидаемое {58.29}, фактическое {actual_total}"))))):
        expected_total = 58.29
        assert actual_total == expected_total, (
            f"Ожидаемая сумма {expected_total},"
            f"но получена {actual_total}"
        )
