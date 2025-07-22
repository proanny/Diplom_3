import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def __init__(self, driver, browser_name):
        super().__init__(driver, browser_name)

    @allure.step('Клик на кнопку Лента заказов')
    def click_to_constructor_button(self):
        self.click_to_element(ConstructorPageLocators.CONSTRUCTOR_PAGE_BUTTON)

    @allure.step('Получение заголовка страница Лента заказов')
    def get_order_title(self):
        return self.find_element_with_wait(ConstructorPageLocators.CONSTRUCTOR_PAGE_TITLE)

    @allure.step('Клик на ингредиент')
    def click_to_ingredient(self):
        self.click_to_element(ConstructorPageLocators.INGREDIENT_BUTTON)

    @allure.step('Получить модальное окно ингредиента')
    def get_ingredient_modal(self):
        return self.find_element_with_wait(ConstructorPageLocators.INGREDIENT_MODAL)

    @allure.step('Закрытие модального окна ингредиента по клику на крестик')
    def close_ingredient_modal(self):
        self.click_to_element(ConstructorPageLocators.INGREDIENT_MODAL_CLOSE)

    @allure.step('Добавление ингредиента')
    def drag_and_drop_element(self, source_element_locator, target_element_locator):
        source_element = self.find_element_with_wait(source_element_locator)
        target_element = self.find_element_with_wait(target_element_locator)

        script = """
        function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragStartEvent);
        
            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            destinationNode.dispatchEvent(dropEvent);
        
            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragEndEvent);
        }
        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """

        self.driver.execute_script(script, source_element, target_element)

    @allure.step('Получение счетчика ингредиента')
    def get_ingredient_counter(self):
        return self.find_element_with_wait(ConstructorPageLocators.INGREDIENT_COUNTER)

    @allure.step('Получение кнопки Оформить заказ')
    def get_create_ingredient_button(self):
        return self.find_element_with_wait(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_create_order_button(self):
        return self.click_to_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получение идентификатора заказа')
    def get_order_id(self):
        WebDriverWait(self.driver, 5).until_not(expected_conditions.text_to_be_present_in_element(ConstructorPageLocators.ORDER_ID, '9999'))

        return self.find_element_with_wait(ConstructorPageLocators.ORDER_ID)

    @allure.step('Закрытие модального окна созданного заказа кликом на крестик')
    def close_order_modal(self):
        self.click_to_element(ConstructorPageLocators.CLOSE_ORDER_MODAL)