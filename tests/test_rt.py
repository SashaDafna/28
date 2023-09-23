# import pytest
from config import *
from conftest import *


# открывается стр. формы Авторизация
def test_authorization_is_exists(auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH


# пункт меню Почта кликабелен и открывает форму авторизации по почте+паролю
def test_mail_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    assert auth.find_element(auth.LOCATOR_INPUT_MAIL)


# базовая позитив.тест авторизации по валидным телефону/почте+паролю
# По умолчанию при открытии страницы открыта форма авторизации по телефону -- таб "Телефон"
# При вводе почты таб "Телефон" переключается на таб "Почта"
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_valid_data(auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_pass)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# авторизация: валидные телефон+почта c некорректным паролем: сообщение об ошибке
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_fake_pass(auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, fake_pass)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# негатив.тест авторизации по пустому полю ввода телефона и валидному паролю: сообщение об ошибке
# негатив.тест авторизации по пустому полю ввода телефона и пустому полю пароля: сообщение об ошибке
@pytest.mark.parametrize('password', [valid_pass, ''], ids=['valid password', 'invalid password (empty input)'])
def test_auth_empty_phone(auth, password):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_PHONE)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_PHONE_MSG


# негатив.тест авторизации по пустому полю ввода почты и валидному паролю: сообщение об ошибке
def test_auth_empty_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_pass)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_MAIL_MSG


# негатив.тест авторизации по пустому полю ввода логина и валидному паролю: сообщение об ошибке
def test_auth_empty_login(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_pass)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LOGIN_MSG


# негатив.тест авторизации по пустому полю ввода лицевого счета и валидному паролю: сообщение об ошибке
def test_auth_empty_ls(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_pass)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LS_MSG


# ссылка Забыл пароль кликабельна и открывает форму Восстановление пароля
def test_forgot_password(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY


# ссылка Зарегистрироваться кликабельна и открывает форму Регистрация
def test_register(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION


# позитив.тест авторизации по валидному телефону+паролю при вводе телефона в таб Почта

@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_pass)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# позитив.тест авторизации по валидному телефону+паролю при вводе телефона в таб "Логин"
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_login(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_pass)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# позитив.тест авторизации по валидному телефону+паролю при вводе телефона в таб "Лицевой счет"
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_ls(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_pass)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert active_tab_name == 'Телефон'
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# позитив.тест перехода к стр.авторизации через VK
def test_auth_social_network_vk(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_VK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_VK)


# позитив.тест перехода к стр.авторизации через Однокласники
def test_auth_social_network_ok(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_OK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_OK)


# позитив.тест перехода к стр.авторизации через Mail.ru
def test_auth_social_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_MAIL)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_MAIL)


# позитив.тест перехода к стр.авторизации через Яндекс
def test_auth_social_yandex(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_YANDEX)
    if auth.find_element(auth.LOCATOR_SOCIAL_YANDEX):
        auth.click_element(auth.LOCATOR_SOCIAL_YANDEX)
        assert auth.find_element(auth.LOCATOR_IDENTIFIER_YANDEX)
    else:
        assert auth.find_element(auth.LOCATOR_IDENTIFIER_YANDEX)


# позитив.тест перехода на страницу пользовательского соглашения
def test_agreement_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_AGREEMENT)
    windows = auth.driver.window_handles
    auth.driver.switch_to.window(windows[-1])
    assert auth.find_element(auth.LOCATOR_AGREEMENT_ROOT)
