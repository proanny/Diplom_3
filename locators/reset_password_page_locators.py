from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    RESET_PASSWORD_LINK = By.XPATH, './/main//a[text()="Восстановить пароль"]'
    EMAIL_INPUT = By.XPATH, './/form[starts-with(@class, "Auth_form_")]//input'
    RESET_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    RESET_PASSWORD_INPUT = By.XPATH, './/form[starts-with(@class, "Auth_form_")]//input[@type="password"]'
    RESET_PASSWORD_INPUT_CONTAINER_ACTIVE = By.XPATH, './/div[contains(@class, "input_status_active")]'
    SHOW_PASSWORD_BUTTON = By.XPATH, './/form[starts-with(@class, "Auth_form_")]//*[@class="input__icon input__icon-action"]'
