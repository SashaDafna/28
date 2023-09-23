import pytest
from selenium import webdriver
from pages.locators import Locators


# создаем фикстуру инициализации браузера Chrome
@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    # типо teardown


# создаем фикстуру авторизации пользователя
@pytest.fixture()
def auth(browser):
    auth = Locators(browser)
    return auth
