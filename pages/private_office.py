import allure

from pages.base_page import BasePage
from locators.accout_page_locators import AccountPageLocators
import data


class PrivateOffice(BasePage):

    @allure.step('клик на кнопку Восстановить пароль')
    def click_recovered_pass(self):
        recover_password_button = self.find_element_with_wait_clickable(AccountPageLocators.recover_password)
        self.click_to_element(recover_password_button)

    @allure.step('получение текста на форме восстановления пароля')
    def get_text_recovered_pass(self):
        self.find_element_with_wait(AccountPageLocators.recovery_password)
        return self.get_text_from_element(AccountPageLocators.recovery_password)

    @allure.step('пвод email на форме восстановления пароля')
    def put_email_on_recovered_pass_form(self):
        self.add_text_to_element(AccountPageLocators.recover_password_email, data.USER_EMAIL)

    @allure.step('Клик на кнопку Восстановить пароль')
    def click_recovered_recovered_pass_form(self):
        recover_password_button = self.find_element_with_wait_clickable(
            AccountPageLocators.recover_password_button)
        self.click_to_element(recover_password_button)

    @allure.step('получение текста на форме восстановления пароля')
    def get_text_on_recovered_pass_form(self):
        self.find_element_with_wait(AccountPageLocators.recovery_password)
        return self.get_text_from_element(AccountPageLocators.recovery_password)

    @allure.step('получение типа поля ввода пароля')
    def get_type_on_recovered_pass_form(self):
        return self.find_elements_with_wait(AccountPageLocators.password_input)[1]

    @allure.step('Активация поля ввода пароля')
    def click_input_pass_field(self):
        password_active_key = self.find_element_with_wait_clickable(
            AccountPageLocators.password_active_key)
        self.click_to_element(password_active_key)

    @allure.step('получение текста на форме личного кабинета')
    def get_text_on_private_office_form(self):
        form_text1 = self.find_element_with_wait(AccountPageLocators.account_form_text1)
        form_text2 = self.find_element_with_wait(AccountPageLocators.account_form_text2)
        return form_text1, form_text2

    @allure.step('клик на кнопку История заказов')
    def click_orders_history(self):
        orders_history_button = self.find_elements_with_wait(
            AccountPageLocators.orders_history)
        self.click_to_element(orders_history_button[1])

    @allure.step('клик на кнопку История закзаов (для firefox)')
    def click_orders_history_firefox(self):
        orders_history_button = self.find_elements_with_wait(
            AccountPageLocators.orders_history)
        self.click_on_web_element_for_firefox(orders_history_button[1])

    @allure.step('получение спсика истории заказов')
    def get_order_history_list(self):
        return len(self.find_elements_with_wait(AccountPageLocators.orders_history_list))

    @allure.step('клик на кнопку logout (для firefox)')
    def click_logout(self):
        if data.DRIVER_NAME == 'chrome':
            logout_button = self.find_element_with_wait_clickable(
                AccountPageLocators.logout_button)
            self.click_to_element(logout_button)
        else:
            self.scroll_try_to_element(AccountPageLocators.logout_button)
            self.click_on_element_for_firefox(AccountPageLocators.logout_button)
