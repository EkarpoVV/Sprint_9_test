from locators.crete_account_locators import CreateAccountPageLocators
from pages.base_page import BasePage
import allure
from urls import *

class CreateAccountPage(BasePage):

    @allure.step("Нажать кнопку Создать аккаунт")
    def click_create_account_button_header(self):
        self.click_to_element(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON_HEADER)

    @allure.step("Заполнить поле Имя")
    def set_name(self,text):
        self.add_text_to_element(CreateAccountPageLocators.FIRST_NAME, text)

    @allure.step("Заполнить поле Фамилия")
    def set_last_name(self,text):
        self.add_text_to_element(CreateAccountPageLocators.LAST_NAME, text)
    
    @allure.step("Заполнить поле Имя пользователя")
    def set_user_name(self,text):
        self.add_text_to_element(CreateAccountPageLocators.USER_NAME_FIELD, text)
    
    @allure.step("Заполнить поле Адрес электронной почты")
    def set_email(self,text):
        self.add_text_to_element(CreateAccountPageLocators.EMAIL_FIELD, text)

    @allure.step("Заполнить поле Пароль")
    def set_password(self,text):
        self.add_text_to_element(CreateAccountPageLocators.PASSWORD_FIELD, text)
    
    @allure.step("Кликнуть Создать аккаунт")
    def click_create_account_button(self,):
        self.click_to_element(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON)

    @allure.step("Открыть главную страницу Рецептов")
    def open_main_page_recipes(self):
        self.go_to_url(BASE_URL)
    