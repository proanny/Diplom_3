import allure
from selenium.webdriver.support.wait import WebDriverWait

from data import UrlForTests
from locators.constructor_page_locators import ConstructorPageLocators
from pages.constructor_page import ConstructorPage

from selenium.webdriver.support import expected_conditions

@allure.suite('Тест конструктора заказа')
class TestConstructorPage:

    @allure.title('Тест перехода на страницу Конструктора заказов')
    def test_go_to_orders_list_page(self, driver):
        page = ConstructorPage(driver[0], driver[1])

        page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        page.click_to_constructor_button()

        assert page.get_order_title()

    @allure.title('Тест отображения всплывающего окна с деталями ингредиента по клику на ингредиент')
    def tests_ingredient_modal(self, driver):
        page = ConstructorPage(driver[0], driver[1])

        page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        page.click_to_constructor_button()

        page.click_to_ingredient()

        assert page.get_ingredient_modal()

    @allure.title('Тест закрытия всплывающего окна с деталями ингредиента по клику на крести')
    def tests_close_ingredient_modal(self, driver):
        page = ConstructorPage(driver[0], driver[1])

        page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        page.click_to_constructor_button()

        page.click_to_ingredient()

        element = page.get_ingredient_modal()

        page.close_ingredient_modal()

        WebDriverWait(driver[0], 5).until(
            expected_conditions.invisibility_of_element(element),
        )

        assert element.is_displayed() == False

    @allure.title('Тест смены счетчика ингредиента после добавления в заказ')
    def tests_add_ingredient_and_change_counter(self, driver):
        page = ConstructorPage(driver[0], driver[1])

        page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        page.click_to_constructor_button()
        counter_old = page.get_ingredient_counter().text

        page.drag_and_drop_element(ConstructorPageLocators.INGREDIENT_BUTTON, ConstructorPageLocators.INGREDIENT_BASKET)
        counter_new = page.get_ingredient_counter().text
        assert counter_old < counter_new

    @allure.title('Тест возможности создания заказа авторизированным пользователем')
    def test_user_can_create_order(self, driver, login):
        page = ConstructorPage(driver[0], driver[1])

        page.click_to_constructor_button()
        page.drag_and_drop_element(ConstructorPageLocators.INGREDIENT_BUTTON, ConstructorPageLocators.INGREDIENT_BASKET)

        assert page.get_create_ingredient_button()