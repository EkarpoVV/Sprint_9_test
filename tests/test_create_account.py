import allure
from generators import Generatorss

class TestCreateAccountPage:

    @allure.title("Регистрация нового пользователя")
    def test_create_account(self, create_account_page, login_page):
        
        create_account_page.open_main_page_recipes()
        create_account_page.click_create_account_button_header()
        create_account_page.set_name(Generatorss.generate_random_string(8))
        create_account_page.set_last_name(Generatorss.generate_random_string(8))
        create_account_page.set_user_name(Generatorss.generate_random_string(8))
        create_account_page.set_email(Generatorss.generate_random_email())
        create_account_page.set_password(Generatorss.generate_random_string(8))
        create_account_page.click_create_account_button()
     
        assert login_page.check_open_login_page()
