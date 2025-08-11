from selenium.webdriver.common.by import By

class OrderPageLocators:
    order_feed = By.XPATH, "//p[text()='Лента Заказов']"  # лента заказов
    order_feed_form = By.XPATH, "//h1[text()='Лента заказов']"  # форма лента заказов
    order_feed_list = By.XPATH, "//li[@class[contains(.,'OrderHistory_listItem__2x95r mb-6')]]"  # список заказов
    order_detail_form = By.XPATH, "//p[text()='Cостав']"  # форма детали заказа
    order_number = By.XPATH, "//h2[@class[contains(.,'Modal_modal__title_shadow__3ikwq')]]"  # номер заказа
    order_form_close_button = By.XPATH, "//button[@class[contains(.,'Modal_modal__close_modified__3V5XS')]]"  # кнопка закрытия формы заказа
    order_done_list = By.XPATH, "//li[@class[contains(.,'text text_type_digits-default mb-2')]]"  # список готовых заказов
    orders_history = By.XPATH, "//a[@class[contains(.,'Account_link__2ETsJ')]]"  # история заказов
    orders_history_list = By.XPATH, "//ul[@class[contains(.,'OrderHistory_profileList')]]"  # история заказов
    orders_history_list_number = By.XPATH, "//p[@class[contains(.,'text text_type_digits-default')]]"  # список номеров заказов
    order_counter_list = By.XPATH, "//p[@class[contains(.,'OrderFeed_number__2MbrQ text text_type_digits-large')]]" # каунтер заказов
    order_inprogress_list = By.XPATH, "//li[@class[contains(.,'text text_type_main-small')]]" # в работе

    orders_feed_button = By.XPATH, "//p[text()='Лента Заказов']"  # кнопка лента заказов
    orders_feed_form = By.XPATH, "//h1[text()='Лента заказов']"  # форма лента заказов
