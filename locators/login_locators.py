from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_PAGE_TEXT = (By.XPATH, "//h1[text()='Войти на сайт']")
    LOGIN_BUTTON_HEADER = (By.XPATH, "//a[text()='Войти']")
