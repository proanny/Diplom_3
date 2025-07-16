import allure

from data import AuthCredentials
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, driver, browser_name):
        super().__init__(driver, browser_name)

    @allure.step('Клик ссылку Восстановить пароль')
    def click_to_account_button(self):
        self.click_to_element(ResetPasswordPageLocators.RESET_PASSWORD_LINK)

    @allure.step('Заполнение Email')
    def set_email(self):
        self.add_text_to_element(ResetPasswordPageLocators.EMAIL_INPUT, AuthCredentials.EMAIL)

    @allure.step('Получение кнопки Восстановить')
    def get_reset_password_button(self):
        self.find_element_with_wait(ResetPasswordPageLocators.RESET_BUTTON)

    @allure.step('Получение поля Пароль')
    def get_reset_password_input(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.RESET_PASSWORD_INPUT)

    @allure.step('Нажатие на кнопку восстановить')
    def click_to_submit_reset_button(self):
        self.click_to_element(ResetPasswordPageLocators.RESET_BUTTON)

    @allure.step('Нажатие кнопку просмотра пароля')
    def click_to_view_password_button(self):
        self.click_to_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Получение активного поля Пароль')
    def get_password_input_active(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.RESET_PASSWORD_INPUT_CONTAINER_ACTIVE)
