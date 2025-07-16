import pytest
from selenium import webdriver

from data import UrlForTests
from locators.constructor_page_locators import ConstructorPageLocators
from locators.main_locators import MainLocators
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        browser_name = 'Chrome'
        driver = webdriver.Chrome()
    else:
        browser_name = 'Firefox'
        driver = webdriver.Firefox()

    yield driver, browser_name
    driver.quit()

@pytest.fixture()
def login(driver):
    page = AccountPage(driver[0], driver[1])
    page.go_to_url(UrlForTests.URL_MAIN_PAGE)
    page.click_to_account_button()
    page.set_email()
    page.set_password()
    page.click_to_login_button()

@pytest.fixture()
def create_order(driver, login):
    page = ConstructorPage(driver[0], driver[1])

    page.click_to_constructor_button()
    page.drag_and_drop_element(ConstructorPageLocators.INGREDIENT_BUTTON, ConstructorPageLocators.INGREDIENT_BASKET)

    page.click_create_order_button()
    page.get_order_id()
    page.wait_element_hidden(MainLocators.LOADER)
    order_id = page.get_order_id().text
    page.close_order_modal()

    yield order_id

