from selenium.webdriver.common.by import By


class MainLocators:
    LOADER = By.XPATH, './/img[@alt="loading animation"]'
    MODAL = By.XPATH, './/section/div[starts-with(@class, "Modal_modal_overlay")]'
    LOADING_TEXT = By.XPATH, './/div[starts-with(@class, "App_centeredComponent") and text()="Загрузка..."]'
