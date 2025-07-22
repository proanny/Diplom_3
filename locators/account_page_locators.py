from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_BUTTON = By.XPATH, '//header/*/a[@href="/account"]'
    ORDERS_HISTORY_BUTTON = By.XPATH, './/ul[starts-with(@class, "Account_list")]//a[text()="История заказов"]'
    ORDERS_HISTORY_LIST_CONTAINER = By.XPATH, './/ul[contains(@class, "OrderHistory_list")]'
    LOGOUT_BUTTON = By.XPATH, './/ul[starts-with(@class, "Account_list")]//button[text()="Выход"]'
    EMAIL_INPUT = By.XPATH, './/form[starts-with(@class, "Auth_form_")]//input[@type="text"]'
    PASSWORD_INPUT = By.XPATH, './/form[starts-with(@class, "Auth_form_")]//input[@type="password"]'
    LOGIN_BUTTON = By.XPATH, './/button[text()="Войти"]'
    ORDER_CARD_BY_ID = By.XPATH, '//div[starts-with(@class, "OrderHistory_textBox")]/p[text()="{}"]'
