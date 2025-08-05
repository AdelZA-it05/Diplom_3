from faker import Faker
fake = Faker("ru_RU")
import allure

import data
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage():

    # переход по клику на «Конструктор»
    @allure.title('переход по клику на «Конструктор»')
    @allure.description('Проверка перехода в конструктор по клику на кнопку конструктор')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_click_on_constructor(self, driver):
        testmainpage = MainPage(driver)
        testmainpage.go_to_url(data.WEB_LINK)

        constructor = testmainpage.find_element_with_wait(MainPageLocators.constructor_button)
        testmainpage.wait_element_to_clickable(constructor)
        testmainpage.click_to_element(constructor)

        assert testmainpage.get_text_from_element(MainPageLocators.constructor_form) == data.CONSTRUCTOR_INFO

    @allure.title('переход по клику на «Лента заказов»')
    @allure.description('Проверка перехода в на ленту заказов по клику на кнопку лента заказов')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_on_order_feed(self, driver):
        testmainpage = MainPage(driver)
        testmainpage.go_to_url(data.WEB_LINK)

        orders_feed = testmainpage.find_element_with_wait(MainPageLocators.orders_feed_button)
        testmainpage.wait_element_to_clickable(orders_feed)
        testmainpage.click_to_element(orders_feed)

        assert testmainpage.get_text_from_element(MainPageLocators.orders_feed_form) == data.ORDER_FEED_INFO

    # если кликнуть на ингредиент, появится всплывающее окно с деталями
    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Проверка отображения информации об ингридиенте')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_click_on_ingredient(self, driver):
        testmainpage = MainPage(driver)
        testmainpage.go_to_url(data.WEB_LINK)

        ingredients_title = testmainpage.find_elements_with_wait(MainPageLocators.ingredients_buns)
        testmainpage.wait_element_to_clickable(ingredients_title[1])
        testmainpage.click_to_element(ingredients_title[1])
        testmainpage.wait_element_to_clickable(ingredients_title[0])
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testmainpage.click_to_element(ingredients_title[0])
        else:
            # firefox
            testmainpage.click_on_web_element_for_firefox(ingredients_title[0])

        ingredients = testmainpage.find_elements_with_wait(MainPageLocators.ingredients_list)
        testmainpage.wait_element_to_clickable(ingredients[0])
        testmainpage.click_to_element(ingredients[0])

        ingredient_info = testmainpage.find_element_with_wait(MainPageLocators.ingredients_list)

        assert ingredient_info.text.split('\n') == data.INGREDIENT_INFO

    @allure.title('всплывающее окно закрывается кликом по крестик')
    @allure.description('Проверка закрытия окна с информацией об ингредиенте по нажатии на крестик')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_close_ingredient_info_window(self, driver):
        testmainpage = MainPage(driver)
        testmainpage.go_to_url(data.WEB_LINK)

        ingredients_title = testmainpage.find_elements_with_wait(MainPageLocators.ingredients_buns)
        testmainpage.wait_element_to_clickable(ingredients_title[1])
        testmainpage.click_to_element(ingredients_title[1])
        testmainpage.wait_element_to_clickable(ingredients_title[0])
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testmainpage.click_to_element(ingredients_title[0])
        else:
            # firefox
            testmainpage.click_on_web_element_for_firefox(ingredients_title[0])

        ingredients = testmainpage.find_elements_with_wait(MainPageLocators.ingredients_list)
        testmainpage.wait_element_to_clickable(ingredients[0])
        testmainpage.click_to_element(ingredients[0])

        ingredients_close = testmainpage.find_elements_with_wait(MainPageLocators.ingredient_info_close)
        testmainpage.wait_element_to_clickable(ingredients_close[0])
        testmainpage.click_to_element(ingredients_close[0])

        assert testmainpage.get_text_from_element(MainPageLocators.constructor_form) == data.CONSTRUCTOR_INFO

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Проверка увеличения каунтера ингридиента при добавлении его в заказ')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_counter_add_this_ingredient(self, driver):
        testmainpage = MainPage(driver)
        testmainpage.go_to_url(data.WEB_LINK)

        ingredient = testmainpage.find_elements_with_wait(MainPageLocators.ingredients_list)
        ingredient_info_before = ingredient[0].text.split()

        testmainpage.drag_and_drop_element(MainPageLocators.ingredients_list, MainPageLocators.burger_constructor_basket)

        ingredient = testmainpage.find_elements_with_wait(MainPageLocators.ingredients_list)
        ingredient_info_after = ingredient[0].text.split()

        assert ingredient_info_before[0] < ingredient_info_after[0]

    @allure.title('залогиненный пользователь может оформить заказ')
    @allure.description('Проверка что, залогиненный пользоватеоь может оформить заказ')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_autorized_user_can_place_order(self, user, driver):
        testmainpage = MainPage(driver)
        testmainpage.go_to_url(data.WEB_LINK)

        text_before = testmainpage.get_text_from_element(MainPageLocators.login_account)
        testmainpage.autorization_user(email=user[2][0], password=user[2][1])
        text_after = testmainpage.get_text_from_element(MainPageLocators.place_order)

        assert text_before == data.TEXT_BEFORE_LOGIN and text_after == data.TEXT_AFTER_LOGIN