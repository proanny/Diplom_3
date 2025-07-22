import allure

from data import UrlForTests
from locators.main_locators import MainLocators
from pages.account_page import AccountPage

@allure.suite('Тест личного кабинета')
class TestAccountPage:
    @allure.title('Тест перехода в личный кабинет')
    def test_go_to_account_page(self, driver):
        page = AccountPage(driver[0], driver[1])
        page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        page.click_to_account_button()

        assert page.get_login_button()

    @allure.title('Тест перехода в историю заказов')
    def test_go_to_orders_history(self, driver, login):
        page = AccountPage(driver[0], driver[1])

        page.wait_element_hidden(MainLocators.LOADER)

        page.click_to_account_button()

        page.wait_element_hidden(MainLocators.LOADER)

        page.click_to_orders_history_button()

        assert page.get_order_history_container()

    @allure.title('Тест выхода из учетной записи')
    def test_logout(self, driver, login):
        page = AccountPage(driver[0], driver[1])

        page.wait_element_hidden(MainLocators.LOADER)

        page.click_to_account_button()
        page.wait_element_hidden(MainLocators.LOADER)

        page.click_to_logout_button()

        assert page.get_login_button()
