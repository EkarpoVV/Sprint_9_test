from selenium.webdriver.common.by import By

class CreateAccountPageLocators:
    FIRST_NAME = (By.NAME, "first_name") 
    LAST_NAME =  (By.NAME, "last_name")
    USER_NAME_FIELD = (By.NAME, "username")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    CREATE_ACCOUNT_BUTTON_HEADER = (By.XPATH, "//a[text()='Создать аккаунт']")
