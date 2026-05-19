import allure
from pathlib import Path
from generators import Generatorss


class TestCreateRecipePage:

    @allure.title("Создание рецепта")
    def test_create_recipe(self,create_and_login_user ,recipe_page,recipe_image):
        recipe_page.click_create_recipe_button_header()
        recipe_name = Generatorss.generate_random_string(8)
        recipe_page.set_recipe_name(recipe_name)
        recipe_page.set_ingredient_name("индейка")
        recipe_page.click_ingredient_name()
        recipe_page.set_ingredient_amount("22")
        recipe_page.click_add_ingredient_button()
        recipe_page.set_coocking_time("33")
        recipe_page.set_recipe_description(Generatorss.generate_random_string(8))
        #CURRENT_DIR = Path(__file__).parent 
        #FILE_PATH = (CURRENT_DIR.parent / "assets" / "test_recipe_image.JPG").resolve()
        recipe_page.upload_recipe_image(str(recipe_image))   #передаем путь файла в метод
        recipe_page.scrol_to_down_create_recipe_button()
        recipe_page.click_create_recipe_button()
        recipe_name_from_new_card = recipe_page.get_recipe_name_after_create_recipe()

        assert recipe_name == recipe_name_from_new_card