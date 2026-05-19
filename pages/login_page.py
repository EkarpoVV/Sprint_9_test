from pages.base_page import BasePage
import allure
from urls import *
from locators.login_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.step("Заполнить поле Электронная почта")
    def set_email(self,text):
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, text)

    @allure.step("Заполнить поле Пароль")
    def set_password(self,text):
        self.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, text)

    @allure.step("Нажать кнопку Войти")
    def click_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Проверка открытия страницы авторизации")
    def check_open_login_page(self):
        try:
            self.find_element_with_wait(LoginPageLocators.LOGIN_PAGE_TEXT)
            return True
        except:
            return False
    
    @allure.step("Нажать кнопку Войти в хедере")
    def click_login_button_header(self):
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON_HEADER)