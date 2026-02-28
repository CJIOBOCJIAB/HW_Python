from selenium.webdriver.common.by import By


class Info:

    def __init__(self, driver):

        self.driver = driver

    def address(self, first_name, last_name, zip_code):

        self.driver.find_element(
            By.CSS_SELECTOR, '[name="firstName"]').send_keys(first_name)
        print("Пользователь : ", first_name)

        self.driver.find_element(
            By.CSS_SELECTOR, '[name="lastName"]').send_keys(last_name)
        print("Пользователь : ", last_name)

        self.driver.find_element(
            By.CSS_SELECTOR, '[name="postalCode"]').send_keys(zip_code)
        print("Индекс : ", zip_code)

    def cont(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="continue"]').click()
        print('Переход к "Overview"')
