from faker import Faker
fake = Faker("ru_RU")
import allure

import data
from pages.account_page import Account
from locators.accout_page_locators import AccountPageLocators


class TestPersonalAccount():

    @allure.title('проверка авторизации существующего  пользователя')
    @allure.description('Проверка что, авторизация пользователя (фикстура user) проходит корректно')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_autorize_user(self, user, driver):
        testpersonalaccount = Account(driver)
        testpersonalaccount.go_to_url(data.WEB_LINK)

        testpersonalaccount.autorization_user(email=user[2][0], password=user[2][1])

        assert testpersonalaccount.get_text_from_element(AccountPageLocators.constructor_form) == data.CONSTRUCTOR_INFO

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    @allure.description('Проверка что, при нажатии кнопки восстановить пароль переходим на страницу восстановления пароля')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_password_recover(self, driver):
        testpersonalaccount = Account(driver)
        testpersonalaccount.go_to_url(data.WEB_LINK)

        personal_account_button = testpersonalaccount.find_element_with_wait_clickable(AccountPageLocators.personal_account)
        testpersonalaccount.click_to_element(personal_account_button)

        recover_password_button = testpersonalaccount.find_element_with_wait_clickable(AccountPageLocators.recover_password)
        testpersonalaccount.click_to_element(recover_password_button)

        testpersonalaccount.find_element_with_wait(AccountPageLocators.recovery_password)

        assert testpersonalaccount.get_text_from_element(AccountPageLocators.recovery_password) == data.RECOVERY_PASSWORD

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Проверка ввода почты и клика по кнопке восстановить')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def testinput_email_click_on_password_recover(self, driver):
        testpersonalaccount = Account(driver)
        testpersonalaccount.go_to_url(data.WEB_LINK)

        personal_account_button = testpersonalaccount.find_element_with_wait_clickable(
            AccountPageLocators.personal_account)
        testpersonalaccount.click_to_element(personal_account_button)

        recover_password_button = testpersonalaccount.find_element_with_wait_clickable(
            AccountPageLocators.recover_password)
        testpersonalaccount.click_to_element(recover_password_button)

        testpersonalaccount.add_text_to_element(AccountPageLocators.recover_password_email, data.USER_EMAIL)

        recover_password_button = testpersonalaccount.find_element_with_wait_clickable(
            AccountPageLocators.recover_password_button)
        testpersonalaccount.click_to_element(recover_password_button)

        testpersonalaccount.find_element_with_wait(AccountPageLocators.recovery_password)

        assert testpersonalaccount.get_text_from_element(
            AccountPageLocators.recovery_password) == data.RECOVERY_PASSWORD

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Проверка активации и деактивации поля ввода пароля')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_click_on_password_make_active(self, driver):
        testpersonalaccount = Account(driver)
        testpersonalaccount.go_to_url(data.WEB_LINK)

        personal_account_button = testpersonalaccount.find_element_with_wait_clickable(
            AccountPageLocators.personal_account)
        testpersonalaccount.click_to_element(personal_account_button)

        password_input_key = testpersonalaccount.find_elements_with_wait(AccountPageLocators.password_input)[1]
        type_before = password_input_key.get_attribute('type')

        password_active_key = testpersonalaccount.find_element_with_wait_clickable(
            AccountPageLocators.password_active_key)
        testpersonalaccount.click_to_element(password_active_key)

        type_after = password_input_key.get_attribute('type')

        assert type_before == 'password' and type_after == 'text'

    @allure.title('переход по клику на «Личный кабинет»')
    @allure.description('Проверка перехода в личный кабинет при клиике на кнопку личный кабинет')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_click_personal_account(self, driver):
        testpersonalaccount = Account(driver)
        testpersonalaccount.go_to_url(data.WEB_LINK)

        personal_account_button = testpersonalaccount.find_element_with_wait_clickable(
            AccountPageLocators.personal_account)
        testpersonalaccount.click_to_element(personal_account_button)

        form_text1 = testpersonalaccount.find_element_with_wait(AccountPageLocators.account_form_text1)
        form_text2 = testpersonalaccount.find_element_with_wait(AccountPageLocators.account_form_text2)

        assert form_text2.text == data.MSG_FORM_PERSONAL_ACCOUNT2 and form_text1.text == data.MSG_FORM_PERSONAL_ACCOUNT1

    @allure.title('переход в раздел «История заказов»')
    @allure.description('Проверка перехода в раздел история заказов при нажатии на историю заказоы в личном кабинете')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_click_orders_history(self, user, driver):
        testpersonalaccount = Account(driver)
        testpersonalaccount.go_to_url(data.WEB_LINK)

        testpersonalaccount.create_order()

        personal_account_button = testpersonalaccount.find_element_with_wait_clickable(
            AccountPageLocators.personal_account)

        if data.DRIVER_NAME == 'chrome':
            testpersonalaccount.click_to_element(personal_account_button)
        else:
            testpersonalaccount.click_on_element_for_firefox(AccountPageLocators.personal_account)

        orders_history_button = testpersonalaccount.find_elements_with_wait(
            AccountPageLocators.orders_history)
        if data.DRIVER_NAME == 'chrome':
            testpersonalaccount.click_to_element(orders_history_button[1])
        else:
            testpersonalaccount.click_on_web_element_for_firefox(orders_history_button[1])

        testpersonalaccount.find_element_with_wait(AccountPageLocators.orders_history_list)

        assert testpersonalaccount.find_element_with_wait(AccountPageLocators.orders_history_list)


    @allure.title('выход из аккаунт')
    @allure.description('Проверка выхода из аккаунта при нажатии выход в личном кабинете')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_click_logout(self, user, driver):
        testpersonalaccount = Account(driver)
        testpersonalaccount.go_to_url(data.WEB_LINK)


        testpersonalaccount.autorization_user(email=user[2][0], password=user[2][1])

        if data.DRIVER_NAME == 'chrome':
            # chrome
            personal_account_button = testpersonalaccount.find_element_with_wait_clickable(
                AccountPageLocators.personal_account)
            testpersonalaccount.click_to_element(personal_account_button)
            # chrome
            logout_button = testpersonalaccount.find_element_with_wait_clickable(
                AccountPageLocators.logout_button)
            testpersonalaccount.click_to_element(logout_button)
        else:
            # firefox
            testpersonalaccount.scroll_try_to_element(AccountPageLocators.personal_account)
            testpersonalaccount.click_on_element_for_firefox(AccountPageLocators.personal_account)

            # firefox
            testpersonalaccount.scroll_try_to_element(AccountPageLocators.logout_button)
            testpersonalaccount.click_on_element_for_firefox(AccountPageLocators.logout_button)


        form_text1 = testpersonalaccount.find_element_with_wait(AccountPageLocators.account_form_text1)
        form_text2 = testpersonalaccount.find_element_with_wait(AccountPageLocators.account_form_text2)

        assert form_text2.text == data.MSG_FORM_PERSONAL_ACCOUNT2 and form_text1.text == data.MSG_FORM_PERSONAL_ACCOUNT1