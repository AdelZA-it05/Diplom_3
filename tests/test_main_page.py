from faker import Faker
fake = Faker("ru_RU")
import allure

import data
from pages.main_page import MainPage


class TestMainPage():

    @allure.title('переход по клику на «Конструктор»')
    @allure.description('Проверка перехода в конструктор по клику на кнопку конструктор')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_click_on_constructor(self, driver):
        testclickonconstructor = MainPage(driver)
        testclickonconstructor.go_to_url(data.WEB_LINK)

        testclickonconstructor.click_constructor()

        assert testclickonconstructor.get_text_on_form_constructor() == data.CONSTRUCTOR_INFO

    @allure.title('переход по клику на «Лента заказов»')
    @allure.description('Проверка перехода в на ленту заказов по клику на кнопку лента заказов')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_on_order_feed(self, driver):
        testorderfeed = MainPage(driver)
        testorderfeed.go_to_url(data.WEB_LINK)

        testorderfeed.click_orders_feed()

        assert testorderfeed.get_text_on_form_orders_feed()  == data.ORDER_FEED_INFO

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Проверка отображения информации об ингридиенте')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_click_on_ingredient(self, driver):
        testclickingredient = MainPage(driver)
        testclickingredient.go_to_url(data.WEB_LINK)
        testclickingredient.click_ingredients_list()


        assert testclickingredient.get_text_ingredient_info() == data.INGREDIENT_INFO

    @allure.title('всплывающее окно закрывается кликом по крестик')
    @allure.description('Проверка закрытия окна с информацией об ингредиенте по нажатии на крестик')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_close_ingredient_info_window(self, driver):
        testcloseingredientwindowe = MainPage(driver)
        testcloseingredientwindowe.go_to_url(data.WEB_LINK)
        testcloseingredientwindowe.click_ingredients_list()

        testcloseingredientwindowe.click_open_ingredient_info()

        testcloseingredientwindowe.click_close_ingredient_info()

        assert testcloseingredientwindowe.get_text_constructor_form() == data.CONSTRUCTOR_INFO

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Проверка увеличения каунтера ингридиента при добавлении его в заказ')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_counter_add_this_ingredient(self, driver):
        testcounteringredient = MainPage(driver)
        testcounteringredient.go_to_url(data.WEB_LINK)

        ingredient_info_before = testcounteringredient.get_ingredient_count_info()

        testcounteringredient.drag_and_drop_ingredient()

        ingredient_info_after = testcounteringredient.get_ingredient_count_info()

        assert ingredient_info_before[0] < ingredient_info_after[0]

    @allure.title('залогиненный пользователь может оформить заказ')
    @allure.description('Проверка что, залогиненный пользоватеоь может оформить заказ')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_autorized_user_can_place_order(self, user, driver):
        testautorizeduserplaceorder = MainPage(driver)
        testautorizeduserplaceorder.go_to_url(data.WEB_LINK)

        text_before = testautorizeduserplaceorder.get_text_before_form()

        testautorizeduserplaceorder.autorization_user(email=user[2][0], password=user[2][1])

        text_after = testautorizeduserplaceorder.get_text_after_form()

        assert text_before == data.TEXT_BEFORE_LOGIN and text_after == data.TEXT_AFTER_LOGIN
