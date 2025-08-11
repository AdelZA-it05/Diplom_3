import allure
from faker import Faker
fake = Faker("ru_RU")

import data
from pages.order_page import OrderPage


class TestOrderPage():

    @allure.title('создание заказа')
    @allure.description('Проверка создания заказа')
    @allure.testcase('Дополнительный тест-кейс Diplom_3')
    def test_create_order(self, user, driver):
        testcounterontime = OrderPage(driver)
        testcounterontime.go_to_url(data.WEB_LINK)

        order_number = testcounterontime.create_order()


        assert order_number != '9999'

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Проверка отображения информвции о заказе')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_details_click_order(self, driver):
        testclickdetails = OrderPage(driver)
        testclickdetails.go_to_url(data.WEB_LINK)

        testclickdetails.click_button_order_feed()

        testclickdetails.click_button_order_detail()

        assert testclickdetails.get_text_order_detail_form() == data.MSG_DETAIL_ORDER

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Проверка отображения заказов из истории заказов в ленте заказов')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_order_history_displayed_order_feed(self, user, driver):
        testhistorydisplayedfeed = OrderPage(driver)
        testhistorydisplayedfeed.go_to_url(data.WEB_LINK)

        order_number = testhistorydisplayedfeed.create_order()

        testhistorydisplayedfeed.click_private_office()

        testhistorydisplayedfeed.click_button_orders_history()

        list_order_history = testhistorydisplayedfeed.get_list_orders_history()

        testhistorydisplayedfeed.click_button_orders_feed()

        list_order_done = testhistorydisplayedfeed.get_list_orders_feed()

        assert order_number in list_order_done and order_number in list_order_history

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается, при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Проверка корректности каунтеров за всё время и за сегодня')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_order_counter_on_time(self, user, driver):
        testcounterontime = OrderPage(driver)
        testcounterontime.go_to_url(data.WEB_LINK)

        testcounterontime.click_orders_feed()

        caunter_all_before = testcounterontime.get_counter_value()[0]
        counter_today_before = testcounterontime.get_counter_value()[1]

        order_number = testcounterontime.create_order()

        testcounterontime.click_orders_feed()

        caunter_all_after = testcounterontime.get_counter_value()[0]
        counter_today_after = testcounterontime.get_counter_value()[1]

        assert counter_today_before < counter_today_after and caunter_all_before < caunter_all_after

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Проверка отображения номера заказа в разделе в работе')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_display_order_in_progress(self, user, driver):
        testdisplayinprogress = OrderPage(driver)
        testdisplayinprogress.go_to_url(data.WEB_LINK)

        testdisplayinprogress.click_inprogress_orders_feed()

        list_order_inprogress_before = testdisplayinprogress.get_listinprogress_orders_feed()

        order_number = testdisplayinprogress.create_order()

        testdisplayinprogress.click_inprogress_orders_feed()

        list_order_inprogress_after = testdisplayinprogress.get_listinprogress_orders_feed()

        assert (order_number not in list_order_inprogress_before and order_number not in list_order_inprogress_after)

    @allure.title('переход по клику на «Лента заказов»')
    @allure.description('Проверка перехода в на ленту заказов по клику на кнопку лента заказов')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    def test_on_order_feed(self, driver):
        testorderfeed = OrderPage(driver)
        testorderfeed.go_to_url(data.WEB_LINK)

        testorderfeed.click_orders_feed()

        assert testorderfeed.get_text_on_form_orders_feed()  == data.ORDER_FEED_INFO











