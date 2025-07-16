from selenium.webdriver.common.by import By


class OrdersListPageLocators:
    ORDER_INGREDIENTS_MODAL_TITLE = By.XPATH, '//p[text()="Cостав"]'
    ORDER_LIST_PAGE_BUTTON = By.XPATH, '//header//a/p[text()="Лента Заказов"]'
    ORDER_PAGE_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDER_CARD = By.XPATH, '//li[starts-with(@class, "OrderHistory_listItem")]'
    ORDER_CARD_BY_ID = By.XPATH, '//div[starts-with(@class, "OrderHistory_textBox")]/p[text()="{}"]'
    ORDER_IN_PROGRESS = By.XPATH, '//li[text()="{}"]'
    ORDERS_COUNTER = By.XPATH, '//p[text()="Выполнено за все время:"]/parent::div/p[starts-with(@class, "OrderFeed_number")]'
    ORDERS_COUNTER_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/parent::div/p[starts-with(@class, "OrderFeed_number")]'
    ORDERS_READY_TEXT = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'
