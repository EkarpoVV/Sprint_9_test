import allure

class TestLoginPage:

    @allure.title("Регистрация нового пользователя")
    def test_login(self, create_user,create_account_page, login_page,recipe_page):
        user_name, user_password = create_user
        create_account_page.open_main_page_recipes()
        login_page.click_login_button_header()
        login_page.set_email(user_name)
        login_page.set_password(user_password)
        login_page.click_login_button()
        
        assert recipe_page.check_logout_button()


