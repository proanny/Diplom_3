import allure

from data import UrlForTests
from locators.constructor_page_locators import ConstructorPageLocators
from locators.main_locators import MainLocators
from locators.orders_list_page_locators import OrdersListPageLocators
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.orders_list_page import OrdersListPage

@allure.suite('Тест ленты заказов')
class TestOrdersListPage:
    @allure.title('Тест перехода на страницу Лента заказов')
    def test_go_to_orders_list_page(self, driver):
        page = OrdersListPage(driver[0], driver[1])

        page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        page.click_to_order_list_button()

        assert page.get_order_title()

    @allure.title('Тест отображения всплывающего окна с деталями по клику на заказ')
    def test_order_modal(self, driver, create_order):
        page = OrdersListPage(driver[0], driver[1])

        page.click_to_order_list_button()
        page.click_to_order_card()
        assert page.get_order_ingredients_title()

    @allure.title('Тест отображения заказа в ленте заказов и истории заказа')
    def test_order_in_order_history_and_in_order_list(self, driver, create_order):
        order_id = create_order
        orders_list_page = OrdersListPage(driver[0], driver[1])
        orders_list_page.click_to_order_list_button()
        orders_list_page.wait_element_hidden(MainLocators.LOADING_TEXT)


        assert orders_list_page.get_order_card_by_id(order_id)

        account_page = AccountPage(driver[0], driver[1])
        account_page.click_to_account_button()
        account_page.wait_element_hidden(MainLocators.LOADER)
        account_page.wait_element_hidden(MainLocators.LOADING_TEXT)
        account_page.click_to_orders_history_button()
        assert account_page.get_order_card_by_id(order_id)

    @allure.title('Тест изменения счетчика заказов после создания заказа')
    def test_orders_counter_change_after_create_order(self, driver, login):
        orders_list_page = OrdersListPage(driver[0], driver[1])

        orders_list_page.wait_element_hidden(MainLocators.LOADER)

        orders_list_page.click_to_order_list_button()

        orders_list_page.wait_element_hidden(MainLocators.LOADING_TEXT)

        counter_source = orders_list_page.get_orders_counter().text

        page = ConstructorPage(driver[0], driver[1])

        page.click_to_constructor_button()
        page.drag_and_drop_element(ConstructorPageLocators.INGREDIENT_BUTTON, ConstructorPageLocators.INGREDIENT_BASKET)

        page.click_create_order_button()
        page.get_order_id()
        page.wait_element_hidden(MainLocators.LOADER)

        page.close_order_modal()

        page.wait_element_hidden(MainLocators.MODAL)

        orders_list_page.click_to_order_list_button()

        counter_target = orders_list_page.get_orders_counter().text
        assert counter_source < counter_target

    @allure.title('Тест изменения счетчика заказов за сегодня после создания заказа')
    def test_today_orders_counter_change_after_create_order(self, driver, login):
        orders_list_page = OrdersListPage(driver[0], driver[1])

        orders_list_page.wait_element_hidden(MainLocators.LOADER)

        orders_list_page.click_to_order_list_button()

        orders_list_page.wait_element_hidden(MainLocators.LOADING_TEXT)

        counter_source = orders_list_page.get_orders_counter_today().text

        page = ConstructorPage(driver[0], driver[1])

        page.click_to_constructor_button()
        page.drag_and_drop_element(ConstructorPageLocators.INGREDIENT_BUTTON, ConstructorPageLocators.INGREDIENT_BASKET)

        page.click_create_order_button()
        page.get_order_id()
        page.wait_element_hidden(MainLocators.LOADER)

        page.close_order_modal()

        page.wait_element_hidden(MainLocators.MODAL)

        orders_list_page.click_to_order_list_button()

        counter_target = orders_list_page.get_orders_counter_today().text
        assert counter_source < counter_target

    @allure.title('Тест перехода заказа в статус В работе после его создания')
    def test_created_order_in_process_status(self, driver, create_order):
        order_id = create_order

        page = OrdersListPage(driver[0], driver[1])
        page.click_to_order_list_button()
        page.wait_element_hidden(MainLocators.LOADING_TEXT)

        page.wait_element_hidden(OrdersListPageLocators.ORDERS_READY_TEXT)

        assert page.get_order_id_in_progress(order_id).text
