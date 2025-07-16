import allure

from locators.orders_list_page_locators import OrdersListPageLocators
from pages.base_page import BasePage


class OrdersListPage(BasePage):
    def __init__(self, driver, browser_name):
        super().__init__(driver, browser_name)

    @allure.step('Клик на кнопку Лента заказов')
    def click_to_order_list_button(self):
        self.click_to_element(OrdersListPageLocators.ORDER_LIST_PAGE_BUTTON)

    @allure.step('Получение заголовка страница Лента заказов')
    def get_order_title(self):
        return self.find_element_with_wait(OrdersListPageLocators.ORDER_PAGE_TITLE)

    @allure.step('Клик на карточку заказа')
    def click_to_order_card(self):
        self.click_to_element(OrdersListPageLocators.ORDER_CARD)

    @allure.step('Получение заголовка состава заказа')
    def get_order_ingredients_title(self):
        return self.find_element_with_wait(OrdersListPageLocators.ORDER_INGREDIENTS_MODAL_TITLE)

    @allure.step('Получение счетчика заказов за всё время')
    def get_orders_counter(self):
        return self.find_element_with_wait(OrdersListPageLocators.ORDERS_COUNTER)

    @allure.step('Получение счетчика заказов за сегодня')
    def get_orders_counter_today(self):
        return self.find_element_with_wait(OrdersListPageLocators.ORDERS_COUNTER_TODAY)

    @allure.step('Получение карточки заказа на странице ленты заказов')
    def get_order_card_by_id(self, id):
        locator = self.format_locators(OrdersListPageLocators.ORDER_CARD_BY_ID, '#0'+id)
        return self.find_element_with_wait(locator)

    @allure.step('Получение номера заказа в статусе В работе')
    def get_order_id_in_progress(self, id):
        locator = self.format_locators(OrdersListPageLocators.ORDER_IN_PROGRESS, id)
        return self.find_element_with_wait(locator)

