from data import AuthCredentials
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage):
    def __init__(self, driver, browser_name):
        super().__init__(driver, browser_name)

    @allure.step('Клик кнопку Личного кабинета')
    def click_to_account_button(self):
        self.click_to_element(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step('Ввод Email')
    def set_email(self):
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, AuthCredentials.EMAIL)

    @allure.step('Получение поля Email')
    def get_login_button(self):
        return self.find_element_with_wait(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Ввод пароля')
    def set_password(self):
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, AuthCredentials.PASSWORD)

    @allure.step('Клик на кнопку Войти')
    def click_to_login_button(self):
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Клик на кнопку Выйти')
    def click_to_logout_button(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Клик на кнопку История заказов')
    def click_to_orders_history_button(self):
        self.click_to_element(AccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Получение контейнера списка заказов')
    def get_order_history_container(self):
        return self.find_element_on_dom_with_wait(AccountPageLocators.ORDERS_HISTORY_LIST_CONTAINER)

    @allure.step('Получение карточки заказа на странице История заказов')
    def get_order_card_by_id(self, id):
        locator = self.format_locators(AccountPageLocators.ORDER_CARD_BY_ID, '#0'+id)
        return self.find_element_with_wait(locator)