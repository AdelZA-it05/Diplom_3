import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import data


class MainPage(BasePage):

    @allure.step('клик на кнопку Конструктор')
    def click_constructor(self):
        constructor = self.find_element_with_wait(MainPageLocators.constructor_button)
        self.wait_element_to_clickable(constructor)
        self.click_to_element(constructor)

    @allure.step('получение текста на форме Конструктор')
    def get_text_on_form_constructor(self):
        return self.get_text_from_element(MainPageLocators.constructor_form)

    @allure.step('клик на список ингридиентов')
    def click_ingredients_list(self):
        ingredients_title = self.find_elements_with_wait(MainPageLocators.ingredients_buns)
        self.wait_element_to_clickable(ingredients_title[1])
        self.click_to_element(ingredients_title[1])
        self.wait_element_to_clickable(ingredients_title[0])
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(ingredients_title[0])
        else:
            self.click_on_web_element_for_firefox(ingredients_title[0])

    @allure.step('Получение текста ingredient_info')
    def get_text_ingredient_info(self):
        ingredient_info = self.find_element_with_wait(MainPageLocators.ingredients_list)
        return ingredient_info.text.split('\n')

    @allure.step('Открытие формы с описанием ингредиента')
    def click_open_ingredient_info(self):
        ingredients = self.find_elements_with_wait(MainPageLocators.ingredients_list)
        self.wait_element_to_clickable(ingredients[0])
        self.scroll_try_to_element(MainPageLocators.ingredients_list)
        self.click_to_element_locator(MainPageLocators.ingredients_list)

    @allure.step('Закрытие формы с описанием ингредиента')
    def click_close_ingredient_info(self):
        ingredients_close = self.find_elements_with_wait(MainPageLocators.ingredient_info_close)
        self.wait_element_to_clickable(ingredients_close[0])
        self.click_to_element(ingredients_close[0])

    @allure.step('Получение текста формы Конструктор')
    def get_text_constructor_form(self):
        return self.get_text_from_element(MainPageLocators.constructor_form)

    @allure.step('Получение значения счётчика тнгрдиента')
    def get_ingredient_count_info(self):
        ingredient = self.find_elements_with_wait(MainPageLocators.ingredients_list)
        return ingredient[0].text.split()

    @allure.step('Собрать бургер')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(MainPageLocators.ingredients_list, MainPageLocators.burger_constructor_basket)


    @allure.step('Получение текста оформления заказа до авторизации')
    def get_text_before_form(self):
        return self.get_text_from_element(MainPageLocators.login_account)

    @allure.step('Получение текста оформления заказа после авторизации')
    def get_text_after_form(self):
        return self.get_text_from_element(MainPageLocators.place_order)
