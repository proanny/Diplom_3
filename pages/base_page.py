from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, browser_name):
        self.driver = driver
        self.browser_name = browser_name

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        (WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    def find_element_on_dom_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_element_hidden(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def click_to_element(self, locator):
        if self.browser_name == 'Chrome':
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()
        else:
            element = WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(locator)
            )

            click = ActionChains(self.driver)
            click.move_to_element(element).click().perform()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_x, str):
        method, locator = locator_x
        locator = locator.format(str)
        return method, locator

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def go_to_last_browser_tab(self):
        self.driver.switch_to(-1)
