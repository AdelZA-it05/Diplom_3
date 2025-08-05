from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import requests
from faker import Faker
fake = Faker()
import allure

import data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 35
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('переход по url')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('поиск элемента с ожиданием кликабельности')
    def find_element_with_wait_clickable(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('клик по элемент локатора')
    def click_to_element_locator(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('клик по web-элементу')
    def click_to_element(self, element):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('добавление текста на элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('добавление текста на web-элемент')
    def add_text_to_web_element(self, web_element, text):
        web_element.send_keys(text)

    @allure.step('получение текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('получение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('ожидание видимости элемента')
    def wait_to_element(self, element_locator):
        self.wait.until(expected_conditions.visibility_of_element_located(element_locator))

    @allure.step('ожидание кликабельности элемента')
    def wait_element_to_clickable(self, element_locator):
        self.wait.until(expected_conditions.element_to_be_clickable(element_locator))

    @allure.step('ожидание элемента по условию')
    def wait_until_condition(self, element_locator, expected_text, is_param):
        if is_param == 0:
            self.wait.until(
                expected_conditions.text_to_be_present_in_element(element_locator, expected_text)
            )
        else:
            self.wait.until_not(
                expected_conditions.text_to_be_present_in_element(element_locator, expected_text)
            )

    @allure.step('клик по локатору кнопки для Firefox')
    def click_on_element_for_firefox(self, locator):
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('клик по web-элементу кнопки для Firefox')
    def click_on_web_element_for_firefox(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('прокрутка элемента')
    def scroll_try_to_element(self, locator):
        """Пролистать страницу до элемента"""
        element = self.find_element_with_wait(locator)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('авторизация пользователя (фикстура user)')
    def autorization_user(self, email=None, password=None):
        if not email: email = (data.USER_EMAIL)
        if not password: password = (data.USER_PASSWORD)
        personal_account_button = self.find_element_with_wait(MainPageLocators.personal_account)
        self.wait_element_to_clickable(personal_account_button)
        self.click_to_element(personal_account_button)
        element_email_password = self.find_elements_with_wait(MainPageLocators.login_param)
        self.add_text_to_web_element(element_email_password[0], email)
        self.add_text_to_web_element(element_email_password[1], password)
        self.click_to_element_locator(MainPageLocators.login_button)
        return email, password

    @allure.step('создание пользователя с использованием API')
    def create_user(self, name=None, email=None, password=None, is_param=0):
        if is_param == 0:
            if not name: name = fake.user_name()
            if not email: email = fake.email()
            if not password: password = fake.password()
        elif is_param == 1:
            name = None
            if not email: email = fake.email()
            if not password: password = fake.password()
        elif is_param == 2:
            if not name: name = fake.user_name()
            email = None
            if not password: password = fake.password()
        elif is_param == 3:
            if not name: name = fake.user_name()
            if not email: email = fake.email()
            password = None
        data_param = {
            "email": email,
            "password": password,
            "name": name
        }
        responce = requests.post(f'{data.BASE_URL}{data.USER_CREATE_URL}', data=data_param)
        try:
            return responce.status_code, responce.json(), [email, password, name]
        except Exception:
            return responce.status_code, responce.text, [email, password, name]

    @allure.step('удаление пользователя')
    def delete_user(self, email=None, password=None):
        responce = self.login_user(email, password)
        p_accesstoken = responce[1]["accessToken"]
        responce = requests.delete(f'{data.BASE_URL}{data.USER_DELETE_URL}', headers={'Authorization': p_accesstoken})
        return responce

    @allure.step('логин пользователя')
    def login_user(self, email=None, password=None):
        data_param = {
            "email": email,
            "password": password
        }

        responce = requests.post(f'{data.BASE_URL}{data.USER_LOGIN_URL}', data=data_param)
        try:
            return responce.status_code, responce.json(), email, password
        except Exception:
            return responce.status_code, responce.text, email, password

    @allure.step('перетаскивание элемента')
    def drag_and_drop_element(self, locator_from, locator_to):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator_from))
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator_to))
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
           var source = arguments[0];
           var target = arguments[1];
           var evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           source.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           target.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           target.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           target.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step('создание заказа')
    def create_order(self):
        self.autorization_user()

        self.drag_and_drop_element(MainPageLocators.ingredients_list,
                                            MainPageLocators.burger_constructor_basket)

        self.find_element_with_wait_clickable(MainPageLocators.place_order)

        self.click_to_element_locator(MainPageLocators.place_order)

        self.wait_until_condition(OrderPageLocators.order_number, '9999', 1)

        order_number = self.get_text_from_element(OrderPageLocators.order_number)

        order_form_close_button = self.find_element_with_wait(OrderPageLocators.order_form_close_button)

        if data.DRIVER_NAME == 'chrome':
            # chrome
            self.click_to_element(order_form_close_button)
        else:
            # firefox
            self.click_on_web_element_for_firefox(order_form_close_button)

        return order_number