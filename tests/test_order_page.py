import pytest
import allure
from faker import Faker
fake = Faker("ru_RU")

import data
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators


class TestOrderPage():

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Проверка отображения информвции о заказе')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_details_click_order(self, driver):
        testorderpage = OrderPage(driver)
        testorderpage.go_to_url(data.WEB_LINK)

        testorderpage.click_to_element_locator(OrderPageLocators.order_feed)

        testorderpage.wait_to_element(OrderPageLocators.order_feed_form)
        order_feed_list = testorderpage.find_elements_with_wait(OrderPageLocators.order_feed_list)
        testorderpage.click_to_element(order_feed_list[0])

        assert testorderpage.find_element_with_wait(OrderPageLocators.order_detail_form)

    # заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Проверка отображения заказов из истории заказов в ленте заказов')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_order_history_displayed_order_feed(self, user, driver):
        testorderpage = OrderPage(driver)
        testorderpage.go_to_url(data.WEB_LINK)

        # создание заказа
        order_number = testorderpage.create_order()

        # история заказов
        personal_account_button = testorderpage.find_element_with_wait_clickable(
            MainPageLocators.personal_account)
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testorderpage.click_to_element(personal_account_button)
        else:
            # firefox
            testorderpage.click_on_web_element_for_firefox(personal_account_button)



        orders_history_button = testorderpage.find_elements_with_wait(
            OrderPageLocators.orders_history)
        testorderpage.click_to_element(orders_history_button[1])

        orders_history_list_number = testorderpage.find_elements_with_wait(OrderPageLocators.orders_history_list_number)
        list_order_history = [_.text[2:] for _ in orders_history_list_number]

        # лента заказов
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testorderpage.click_to_element_locator(MainPageLocators.orders_feed_button)
        else:
            # firefox
            testorderpage.click_on_element_for_firefox(MainPageLocators.orders_feed_button)


        order_done_list = testorderpage.find_elements_with_wait(OrderPageLocators.order_done_list)
        list_order_done = [_.text[1:] for _ in order_done_list]

        assert order_number in list_order_done and order_number in list_order_history

    # при создании нового заказа счётчик Выполнено за всё время увеличивается
    # при создании нового заказа счётчик Выполнено за сегодня увеличивается

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается, при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Проверка корректности каунтеров за всё время и за сегодня')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @pytest.mark.parametrize('is_param', [0, 1])
    def test_order_counter_on_time(self, user, driver, is_param):
        testorderpage = OrderPage(driver)
        testorderpage.go_to_url(data.WEB_LINK)

        # лента заказов
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testorderpage.click_to_element_locator(MainPageLocators.orders_feed_button)
        else:
            # firefox
            testorderpage.click_on_element_for_firefox(MainPageLocators.orders_feed_button)

        # каунтер за всё время/за сегодня
        caunter_list = testorderpage.find_elements_with_wait(OrderPageLocators.order_counter_list)
        caunter_all_before = caunter_list[0].text
        counter_today_before = caunter_list[1].text

        # создание заказа
        order_number = testorderpage.create_order()

        # лента заказов
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testorderpage.click_to_element_locator(MainPageLocators.orders_feed_button)
        else:
            # firefox
            testorderpage.click_on_element_for_firefox(MainPageLocators.orders_feed_button)

        # каунтер за всё время/за сегодня
        caunter_list = testorderpage.find_elements_with_wait(OrderPageLocators.order_counter_list)
        caunter_all_after = caunter_list[0].text
        counter_today_after = caunter_list[1].text

        if is_param == 0:
            assert counter_today_before < counter_today_after
        else:
            assert caunter_all_before < caunter_all_after

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Проверка отображения номера заказа в разделе в работе')
    @allure.testcase('Тест-кейс из Дипломного задания Diplom_3')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_display_order_in_progress(self, user, driver):
        testorderpage = OrderPage(driver)
        testorderpage.go_to_url(data.WEB_LINK)

        # лента заказов
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testorderpage.click_to_element_locator(MainPageLocators.orders_feed_button)
        else:
            # firefox
            testorderpage.scroll_try_to_element(MainPageLocators.orders_feed_button)
            testorderpage.click_on_element_for_firefox(MainPageLocators.orders_feed_button)

        # в работе
        order_inprogress_list = testorderpage.find_elements_with_wait(OrderPageLocators.order_inprogress_list)
        list_order_inprogress_before = [_.text for _ in order_inprogress_list]

        # создание заказа
        order_number = testorderpage.create_order()

        # лента заказов
        if data.DRIVER_NAME == 'chrome':
            # chrome
            testorderpage.click_to_element_locator(MainPageLocators.orders_feed_button)
        else:
            # firefox
            testorderpage.scroll_try_to_element(MainPageLocators.orders_feed_button)
            testorderpage.click_on_element_for_firefox(MainPageLocators.orders_feed_button)

        # в работе
        order_inprogress_list = testorderpage.find_elements_with_wait(OrderPageLocators.order_inprogress_list)
        list_order_inprogress_after = [_.text for _ in order_inprogress_list]

        assert (order_number not in list_order_inprogress_before and order_number not in list_order_inprogress_after)










