from selenium.webdriver.common.by import By
from pages.base import BasePage


class Locators(BasePage):
    # название страницы cправа
    LOCATOR_PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # кнопка Телефон
    LOCATOR_BTN_PHONE = (By.ID, "t-btn-tab-phone")

    # кнопка Почта
    LOCATOR_BTN_MAIL = (By.ID, "t-btn-tab-mail")

    # кнопка Войти
    LOCATOR_BTN_LOGIN = (By.ID, "t-btn-tab-login")

    # кнопка ЛС
    LOCATOR_BTN_LS = (By.ID, "t-btn-tab-ls")

    # поле ввода почты
    LOCATOR_INPUT_MAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')

    # поле ввода имени пользователя
    LOCATOR_INPUT_USERNAME = (By.ID, 'username')

    # поле ввода пароля
    LOCATOR_INPUT_PASSWORD = (By.ID, 'password')

    # кнопка Войти
    LOCATOR_BTN_ENTER = (By.ID, 'kc-login')

    # кнопка Выйти
    LOCATOR_BTN_LOGOUT = (By.ID, 'logout-btn')

    # сообщение ошибки
    LOCATOR_ERROR_MSG = (By.XPATH, "//span[@id='form-error-message']")

    # сообщение что нет имени пользователя
    LOCATOR_EMPTY_USERNAME_MSG = (By.CSS_SELECTOR, '.rt-input-container__meta--error')

    # кнопка Забыли пароль
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')

    # кнопка Зарегистрироваться
    LOCATOR_REGISTER = (By.XPATH, "//a[@id='kc-register']")

    # активная вкладка
    LOCATOR_ACTIVE_TAB = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')

    # кнопка VK
    LOCATOR_SOCIAL_NETWORK_VK = (By.ID, "oidc_vk")

    # ID VK
    LOCATOR_IDENTIFIER_VK = (By.XPATH, "// div[contains(text(), 'Вход в VK ID')]")

    # кнопка Одноклассники
    LOCATOR_SOCIAL_NETWORK_OK = (By.ID, "oidc_ok")

    # ID Одноклассники
    LOCATOR_IDENTIFIER_OK = (By.XPATH, "//div[contains(text(),'Одноклассники')]")

    # кнопка Мой Мир
    LOCATOR_SOCIAL_MAIL = (By.ID, "oidc_mail")

    # ID Мой Мир
    LOCATOR_IDENTIFIER_MAIL = (By.XPATH, "// span[contains(text(), 'Мой Мир@Mail.Ru')]")

    # кнопка Яндекс
    LOCATOR_SOCIAL_YANDEX = (By.ID, "oidc_ya")

    # ID Яндекс
    LOCATOR_IDENTIFIER_YANDEX = (By.XPATH, "//*[@id='UserEntryFlow']/form/div/div[1]/h1")

    # вкладка пользовательского соглашения
    LOCATOR_AGREEMENT = (By.XPATH, "//a[@class='rt-link rt-link--orange' "
                                   "and @href='https://b2c.passport.rt.ru/sso-static/agreement/agreement.html']")

    # идентификатор текста пользовательского соглашения
    LOCATOR_AGREEMENT_ROOT = (By.ID, "root")

    # сообщение ошибки с неверными данными
    ERROR_MSG_INVALID_DATA = 'Неверный логин или пароль'

    # сообщение ошибки с неверной каптчей
    ERROR_MSG_INVALID_CAPTCHA = 'Неверно введен текст с картинки'

    # сообщение что нет номера телефона
    EMPTY_PHONE_MSG = 'Введите номер телефона'

    # сообщение что нет почты
    EMPTY_MAIL_MSG = 'Введите адрес, указанный при регистрации'

    # сообщение что нет имени пользователя
    EMPTY_LOGIN_MSG = 'Введите логин, указанный при регистрации'

    # сообщение что нет ЛС
    EMPTY_LS_MSG = 'Введите номер вашего лицевого счета'

    # название страницы авторизации
    TITLE_AUTH = 'Авторизация'

    # название страницы восстановления пароля
    TITLE_RECOVERY = 'Восстановление пароля'

    # название страницы регистрации
    TITLE_REGISTRATION = 'Регистрация'
