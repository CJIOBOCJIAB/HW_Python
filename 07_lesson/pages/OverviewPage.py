import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Description:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)
        self.actual_total = None

    def total(self):

        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-test="total-label"]')))
        result = total_element.get_attribute("textContent").strip()

        sum_match = re.search(r'\$(\d+\.\d{2})', result)
        actual_total = float(sum_match.group(1))
        print(f"Итоговая сумма : {actual_total}")
        return actual_total
