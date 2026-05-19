from pages.base_page import BasePage
import allure
from urls import *
from locators.login_locators import LoginPageLocators
from locators.create_recipe_locators import CreateRecipePageLocators

class RecipePage(BasePage):

    @allure.step("Проверка отображения кнопки Выход")
    def check_logout_button(self):
        try:
            self.find_element_with_wait(CreateRecipePageLocators.LOGOUT_BUTTON)
            return True
        except:
            return False
    
    @allure.step("Нажать кнопку Создать рецепт в Хедере")
    def click_create_recipe_button_header(self):
        self.click_to_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON_HEADER)
    
    @allure.step("Заполнить поле Название рецепта")
    def set_recipe_name(self,text):
        self.add_text_to_element(CreateRecipePageLocators.RECIPE_NAME_FIELD, text)
    
    @allure.step("Заполнить поле Ингредиенты")
    def set_ingredient_name(self,text):
        self.add_text_to_element(CreateRecipePageLocators.INGREDIENTS_FIELD, text)

    @allure.step("Выбрать Ингредиент из выпадающего списка")
    def click_ingredient_name(self):
        self.click_to_element(CreateRecipePageLocators.FIRST_INGREDIENT)

    @allure.step("Заполнить поле Вес ингредиента")
    def set_ingredient_amount(self,text):
        self.add_text_to_element(CreateRecipePageLocators.INGREDIENTS_AMOUNT_FIELD, text)

    @allure.step("Нажать кнопку Добавить ингредиента")
    def click_add_ingredient_button(self):
        self.click_to_element(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)  

    @allure.step("Заполнить поле Время приготовления")
    def set_coocking_time(self,text):
        self.add_text_to_element(CreateRecipePageLocators.COOCING_TIME_FIELD, text)
        
    @allure.step("Заполнить поле Описание рецепта")
    def set_recipe_description(self,text):
        self.add_text_to_element(CreateRecipePageLocators.RECIPE_DESCRIPTION_FILD, text)

    ## Загрузит фото

    @allure.step("Загрузить картинку рецепта")
    def upload_recipe_image(self, path_to_file):
        element = self.driver.find_element(*CreateRecipePageLocators.UPLOAD_RECIPE_IMAGE) 
        element.send_keys(path_to_file) 

    @allure.step("Нажать кнопку Создать рецепт")
    def click_create_recipe_button(self):
        self.click_to_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)
    
    @allure.step("Прокрутить до кнопки Создать рецепт в низу страницы")
    def scrol_to_down_create_recipe_button(self):
        self.scroll_to_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)   

    @allure.step("Получить название рецепта после его создания")
    def get_recipe_name_after_create_recipe(self):
        return self.get_text_from_element(CreateRecipePageLocators.RECIPE_NAME_AFTER_CREAT_RECIPE)
    
