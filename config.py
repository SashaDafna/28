from faker import Faker


# тестим сайт Ростелекома
URL = 'https://b2c.passport.rt.ru'


# валидные данные авторизации
valid_email = 'TEST_VALID_EMAIL (demdragonyaru@gmail.com)'
valid_phone = 'TEST_VALID_PHONE (+79199081844)'
valid_pass = 'TEST_VALID_PASSWORD'


# некорректные данные авторизации нам генерит
fake = Faker()
fake_pass = fake.password()