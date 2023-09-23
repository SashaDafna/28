from config import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не найдено по локатору {locator}"
        )

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_data(self, locator, text):
        self.find_element(locator).send_keys(text)

    def out(self, driver):
        return self.driver.switch_to.window(driver.window_handles[1])
