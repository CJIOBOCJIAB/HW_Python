from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):

        self.driver = driver

    def checkout(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="checkout"]').click()
        print('Переход к "Your Information"')
