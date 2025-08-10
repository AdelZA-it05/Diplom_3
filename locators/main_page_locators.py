from selenium.webdriver.common.by import By

class MainPageLocators:
    personal_account = By.XPATH, "//p[text()='Личный Кабинет']" # личный кабинет
    login_param = By.XPATH, "//input[@class[contains(.,'text input__textfield')]]"  # email авторизации
    login_button = By.XPATH, "//button[text()='Войти']"  # кнопка войти
    logout_button = By.XPATH, "//button[text()='Выход']"  # кнопка войти

    constructor_button = By.XPATH, "//p[text()='Конструктор']" # кнопка конструктор
    constructor_form = By.XPATH, "//h1[text()='Соберите бургер']"  # форма конструктора

    login_account = By.XPATH, "//button[text()='Войти в аккаунт']"  # формить заказ
    place_order = By.XPATH, "//button[text()='Оформить заказ']"  # формить заказ

    ingredients_buns = By.XPATH, "//div[@class[contains(.,'tab_tab__1SPyG')]]"  # вкладка булки
    ingredients_list = By.XPATH, "//a[@class[contains(.,'BurgerIngredient_ingredient__1TVf6')]]"  # список булок
    ingredients_info = By.XPATH, "//h2[text()='Детали ингредиента']"  # детали ингредиента

    burger_constructor_basket = By.XPATH, "//ul[@class[contains(.,'BurgerConstructor_basket__list__l9dp_')]]" # подготовка заказа

    ingredient_info_close = By.XPATH, "//button[@class[contains(.,'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]]"  # список булок


