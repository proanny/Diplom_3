from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    CONSTRUCTOR_PAGE_BUTTON = By.XPATH, '//header//a/p[text()="Конструктор"]'
    CONSTRUCTOR_PAGE_TITLE =By.XPATH, '//h1[text()="Соберите бургер"]'

    INGREDIENT_BUTTON = By.XPATH, '(//a[starts-with(@class, "BurgerIngredient_ingredient")])[1]'
    INGREDIENT_MODAL = By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]//div[starts-with(@class, "Modal_modal__container")]'
    INGREDIENT_MODAL_CLOSE = By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]//div[starts-with(@class, "Modal_modal__container")]//button[starts-with(@class, "Modal_modal__close_modified")]'
    INGREDIENT_COUNTER = By.XPATH, '(//a[starts-with(@class, "BurgerIngredient_ingredient")])[1]//p[starts-with(@class, "counter_counter__num")]'
    INGREDIENT_BASKET = By.XPATH, '//ul[starts-with(@class, "BurgerConstructor_basket__list")]'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_ID = By.XPATH, '//h2[contains(@class, "Modal_modal__title")]'
    CLOSE_ORDER_MODAL = By.XPATH, '//button[contains(@class, "Modal_modal__close")]'

    ORDER_HISTORY_BUTTON = By.XPATH, '//button[contains(@class, "Modal_modal__close")]'
