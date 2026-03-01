import pytest
from selenium import webdriver


from pages.AuthorizationPage import Authorization
from pages.ProductsPage import Product
from pages.CartPage import Cart
from pages.InformationPage import Info
from pages.OverviewPage import Description


@pytest.fixture
def browser():
    # Настройка браузера FireFox
    driver = webdriver.Firefox()
    driver.set_window_size(1900, 1000)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_buy_shop(browser):

    auth = Authorization(browser)
    add = Product(browser)
    cart = Cart(browser)
    info = Info(browser)
    value = Description(browser)

    auth.params('standard_user', 'secret_sauce')
    auth.login()

    add.add_to_cart('Sauce Labs Backpack')
    add.add_to_cart('Sauce Labs Bolt T-Shirt')
    add.add_to_cart('Sauce Labs Onesie')

    add.go_to_cart()

    cart.checkout()

    info.address('Илья', 'Словослав', '1234567890')
    info.cont()

    actual_total = value.total()
    expected_total = 58.29

    assert actual_total == expected_total
