from faker import Faker
fake = Faker("ru_RU")
import allure

import data
from pages.private_office import PrivateOffice
from locators.accout_page_locators import AccountPageLocators


class TestPrivateOffice():

    @allure.title('проверка авторизации существующего  пользователя')
    @allure.description('Проверка что, авторизация пользователя (фикстура user) проходит корректно')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_autorize_user(self, user, driver):
        testautorizeuser = PrivateOffice(driver) #
        testautorizeuser.go_to_url(data.WEB_LINK)

        testautorizeuser.autorization_user(email=user[2][0], password=user[2][1])

        assert testautorizeuser.get_text_from_element(AccountPageLocators.constructor_form) == data.CONSTRUCTOR_INFO

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    @allure.description('Проверка что, при нажатии кнопки восстановить пароль переходим на страницу восстановления пароля')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_password_recover(self, driver):
        testpasswordrecover = PrivateOffice(driver)
        testpasswordrecover.go_to_url(data.WEB_LINK)

        testpasswordrecover.click_private_office()

        testpasswordrecover.click_recovered_pass()

        text_recovered_pass = testpasswordrecover.get_text_recovered_pass()

        assert text_recovered_pass == data.RECOVERY_PASSWORD


    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Проверка ввода почты и клика по кнопке восстановить')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_input_email_click_on_password_recover(self, driver):
        testclickrecover = PrivateOffice(driver)
        testclickrecover.go_to_url(data.WEB_LINK)

        testclickrecover.click_private_office()

        testclickrecover.click_recovered_pass()

        testclickrecover.put_email_on_recovered_pass_form()

        testclickrecover.click_recovered_recovered_pass_form()

        text_recovered_pass = testclickrecover.get_text_on_recovered_pass_form()

        assert text_recovered_pass == data.RECOVERY_PASSWORD

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Проверка активации и деактивации поля ввода пароля')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_click_on_password_make_active(self, driver):
        testactivepassword = PrivateOffice(driver)
        testactivepassword.go_to_url(data.WEB_LINK)

        testactivepassword.click_private_office()

        password_input_key = testactivepassword.get_type_on_recovered_pass_form()
        type_before = password_input_key.get_attribute('type')

        testactivepassword.click_input_pass_field()

        type_after = password_input_key.get_attribute('type')

        assert type_before == 'password' and type_after == 'text'

    @allure.title('переход по клику на «Личный кабинет»')
    @allure.description('Проверка перехода в личный кабинет при клиике на кнопку личный кабинет')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_click_personal_account(self, driver):
        testprivateoffice = PrivateOffice(driver)
        testprivateoffice.go_to_url(data.WEB_LINK)

        testprivateoffice.click_private_office()

        form_text1, form_text2 = testprivateoffice.get_text_on_private_office_form()

        assert form_text2.text == data.MSG_FORM_PERSONAL_ACCOUNT2 and form_text1.text == data.MSG_FORM_PERSONAL_ACCOUNT1

    @allure.title('переход в раздел «История заказов»')
    @allure.description('Проверка перехода в раздел история заказов при нажатии на историю заказоы в личном кабинете')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_click_orders_history(self, user, driver):
        testordershistory = PrivateOffice(driver)
        testordershistory.go_to_url(data.WEB_LINK)

        testordershistory.create_order()

        testordershistory.click_private_office()

        if data.DRIVER_NAME == 'chrome':
            testordershistory.click_orders_history()
        else:
            testordershistory.click_orders_history_firefox()
        assert testordershistory.get_order_history_list() > 0


    @allure.title('выход из аккаунт')
    @allure.description('Проверка выхода из аккаунта при нажатии выход в личном кабинете')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_click_logout(self, user, driver):
        testclicklogout = PrivateOffice(driver)
        testclicklogout.go_to_url(data.WEB_LINK)

        testclicklogout.autorization_user(email=user[2][0], password=user[2][1])

        testclicklogout.click_private_office()
        testclicklogout.click_logout()

        form_text1, form_text2 = testclicklogout.get_text_on_private_office_form()

        assert form_text2.text == data.MSG_FORM_PERSONAL_ACCOUNT2 and form_text1.text == data.MSG_FORM_PERSONAL_ACCOUNT1
