import allure
from pathlib import Path
#from pages.upload_page import UploadPage
from generators import Generatorss
#import time



class TestCreateRecipePage:

    # Определяем путь здесь, так как файл лежит рядом с тестом


    @allure.title("Создание рецепта")
    def test_create_recipe(self,create_and_login_user ,recipe_page):
        recipe_page.click_create_recipe_button_header()
        recipe_name = Generatorss.generate_random_string(8)
        recipe_page.set_recipe_name(recipe_name)
        recipe_page.set_ingredient_name("индейка") # добавить клик на выпадающий список
        recipe_page.click_ingredient_name()
        recipe_page.set_ingredient_amount("22")
        recipe_page.click_add_ingredient_button()
        recipe_page.set_coocking_time("33")
        recipe_page.set_recipe_description(Generatorss.generate_random_string(8))
        CURRENT_DIR = Path(__file__).parent 
        FILE_PATH = (CURRENT_DIR.parent / "assets" / "test_recipe_image.JPG").resolve()
        recipe_page.upload_recipe_image(str(FILE_PATH))   #передаем путь файла в метод
        recipe_page.scrol_to_down_create_recipe_button()
        recipe_page.click_create_recipe_button()
        recipe_name_from_new_card = recipe_page.get_recipe_name_after_create_recipe()

        assert recipe_name == 2 #recipe_name_from_new_card

    





    ## Загрузит фото

   # @allure.step("Нажать кнопку Создать рецепт")
   # def click_create_recipe_button(self):
   #     self.click_to_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)
