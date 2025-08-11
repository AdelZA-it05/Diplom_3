import allure

import data

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('клик на кнопку Лента заказов')
    def click_button_order_feed(self):
        self.click_to_element_locator(OrderPageLocators.order_feed)

    @allure.step('клик заказ и открытие деталей заказа')
    def click_button_order_detail(self):
        self.wait_to_element(OrderPageLocators.order_feed_form)
        order_feed_list = self.find_elements_with_wait(OrderPageLocators.order_feed_list)
        self.click_to_element(order_feed_list[0])

    @allure.step('получение текста на форме деталей заказа')
    def get_text_order_detail_form(self):
        return self.find_element_with_wait(OrderPageLocators.order_detail_form).text

    @allure.step('клик на кнопку История заказов')
    def click_button_orders_history(self):
        orders_history_button = self.find_elements_with_wait(OrderPageLocators.orders_history)
        self.click_to_element(orders_history_button[1])

    @allure.step('получение списка историй заказа')
    def get_list_orders_history(self):
        orders_history_list_number = self.find_elements_with_wait(OrderPageLocators.orders_history_list_number)
        list_order_history = [_.text[2:] for _ in orders_history_list_number]
        return list_order_history

    @allure.step('клик на кнопку Лента заказов')
    def click_button_orders_feed(self):
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element_locator(OrderPageLocators.orders_feed_button)
        else:
            self.scroll_try_to_element(OrderPageLocators.orders_feed_button)
            self.click_on_element_for_firefox(OrderPageLocators.orders_feed_button)

    @allure.step('получение списка историй заказа')
    def get_list_orders_feed(self):
        order_done_list = self.find_elements_with_wait(OrderPageLocators.order_done_list)
        list_order_done = [_.text[1:] for _ in order_done_list]
        return list_order_done

    @allure.step('получение списка заказов в работе ')
    def get_listinprogress_orders_feed(self):
        order_inprogress_list = self.find_elements_with_wait(OrderPageLocators.order_inprogress_list)
        list_order_inprogress_before = [_.text for _ in order_inprogress_list]
        return list_order_inprogress_before

    @allure.step('клик по ленте заявок')
    def click_inprogress_orders_feed(self):
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element_locator(OrderPageLocators.orders_feed_button)
        else:
            self.click_on_element_for_firefox(OrderPageLocators.orders_feed_button)

    @allure.step('Полученипе счётчиков заявок')
    def get_counter_value(self):
        caunter_list = self.find_elements_with_wait(OrderPageLocators.order_counter_list)
        return caunter_list[0].text, caunter_list[1].text

    @allure.step('клик на кнопку Лента заказов')
    def click_orders_feed(self):
        orders_feed = self.find_element_with_wait(OrderPageLocators.orders_feed_button)
        self.wait_element_to_clickable(orders_feed)
        self.click_to_element(orders_feed)

    @allure.step('получение текста на форме Лента заказов')
    def get_text_on_form_orders_feed(self):
        return self.get_text_from_element(OrderPageLocators.order_feed_form)