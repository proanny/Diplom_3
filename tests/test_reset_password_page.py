import allure

from data import UrlForTests
from pages.account_page import AccountPage
from pages.reset_password_page import ResetPasswordPage

@allure.suite('Тест восстановления пароля')
class TestResetPasswordPage:
    @allure.title('Тест перехода на страницу Восстановления пароля по кнопке Восстановить пароль')
    def test_go_to_reset_password_page(self, driver):
        account_page = AccountPage(driver[0], driver[1])

        account_page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        account_page.click_to_account_button()

        reset_password_page = ResetPasswordPage(driver[0], driver[1])

        reset_password_page.click_to_account_button()

        assert reset_password_page.get_reset_password_button

    @allure.title('Тест ввода почты и клика по кнопке Восстановить')
    def test_set_email_and_click_reset_button(self, driver):
        account_page = AccountPage(driver[0], driver[1])

        account_page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        account_page.click_to_account_button()

        reset_password_page = ResetPasswordPage(driver[0], driver[1])

        reset_password_page.click_to_account_button()

        reset_password_page.set_email()

        reset_password_page.click_to_submit_reset_button()

        assert reset_password_page.get_reset_password_input()

    @allure.title('Тест подсвечивания поля Пароль, при клике по кнопке показать/скрыть пароль')
    def test_reset_password_input_active(self, driver):
        account_page = AccountPage(driver[0], driver[1])

        account_page.go_to_url(UrlForTests.URL_MAIN_PAGE)
        account_page.click_to_account_button()

        reset_password_page = ResetPasswordPage(driver[0], driver[1])

        reset_password_page.click_to_account_button()

        reset_password_page.set_email()

        reset_password_page.click_to_submit_reset_button()

        assert reset_password_page.get_reset_password_input()