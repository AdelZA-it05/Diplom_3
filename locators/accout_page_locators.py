from selenium.webdriver.common.by import By

class AccountPageLocators:

    personal_account = By.XPATH, "//p[text()='Личный Кабинет']" # личный кабинет
    login_param = By.XPATH, "//input[@class[contains(.,'text input__textfield')]]"  # email авторизации
    login_button = By.XPATH, "//button[text()='Войти']"  # кнопка войти
    logout_button = By.XPATH, "//button[text()='Выход']"  # кнопка войти

    account_form_text1 = By.XPATH, "//a[text()='Зарегистрироваться']"  # форма Личный Кабинет
    account_form_text2 = By.XPATH, "//a[text()='Восстановить пароль']"  # форма Личный Кабинет

    constructor_button = By.XPATH, "//p[text()='Конструктор']" # кнопка конструктор
    constructor_form = By.XPATH, "//h1[text()='Соберите бургер']"  # форма конструктора

    recover_password = By.XPATH, "//a[text()='Восстановить пароль']"  # восстановить пароль
    recover_password_email = By.XPATH, "//input[@class[contains(.,'text input__textfield')]]"
    recover_password_button = By.XPATH, "//button[text()='Восстановить']"  # восстановить пароль
    recovery_password = By.XPATH, "//h2[text()='Восстановление пароля']"  # восстановление пароля

    password_active_key = By.XPATH, "//div[@class[contains(.,'input__icon input__icon-action')]]"
    password_input = By.XPATH, "//input[@class[contains(.,'text input__textfield text_type_main-default')]]"

    orders_history = By.XPATH, "//a[@class[contains(.,'Account_link__2ETsJ')]]" # история заказов
    orders_history_list = By.XPATH, "//ul[@class[contains(.,'OrderHistory_profileList')]]"  # история заказов
