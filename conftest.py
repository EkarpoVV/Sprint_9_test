import pytest
from selenium import webdriver
from urls import *
from pages.login_page import LoginPage
from pages.create_account_page import CreateAccountPage
from generators import Generatorss
from pages.recipe_page import RecipePage


from selenium.webdriver.remote.file_detector import LocalFileDetector
from config import BROWSER_NAME, BROWSER_VERSION, SELENOID_URL


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    if SELENOID_URL:
        options.set_capability("browserName", BROWSER_NAME)
        options.set_capability("browserVersion", BROWSER_VERSION)
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": False,
                "sessionTimeout": "3m",
            },
        )
        browser = webdriver.Remote(
            command_executor=SELENOID_URL,
            options=options,
        )
        browser.file_detector = LocalFileDetector()
    else:
        browser = webdriver.Chrome(options=options)

    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()



"""
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()


@pytest.fixture(params=['Chrome','Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.browser_name = request.param

    yield driver
    driver.quit()
"""


@pytest.fixture()
def create_account_page(driver):
    create_account_page = CreateAccountPage(driver)
    return create_account_page

@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture()
def recipe_page(driver):
    recipe_page = RecipePage(driver)
    return recipe_page

@pytest.fixture()
def create_user(create_account_page):
        
    create_account_page.open_main_page_recipes()
    create_account_page.click_create_account_button_header()
    create_account_page.set_name(Generatorss.generate_random_string(8))
    create_account_page.set_last_name(Generatorss.generate_random_string(8))
    user_name = Generatorss.generate_random_string(8)
    create_account_page.set_user_name(user_name)
    create_account_page.set_email(Generatorss.generate_random_email())
    user_password = Generatorss.generate_random_string(8)
    create_account_page.set_password(user_password)
    create_account_page.click_create_account_button()
    
    return  user_name, user_password
    # Удаления узера в этом задании нет

@pytest.fixture()
def create_and_login_user(create_account_page,login_page):
        
    create_account_page.open_main_page_recipes()
    create_account_page.click_create_account_button_header()
    create_account_page.set_name(Generatorss.generate_random_string(8))
    create_account_page.set_last_name(Generatorss.generate_random_string(8))
    user_name = Generatorss.generate_random_string(8)
    create_account_page.set_user_name(user_name)
    create_account_page.set_email(Generatorss.generate_random_email())
    user_password = Generatorss.generate_random_string(8)
    create_account_page.set_password(user_password)
    create_account_page.click_create_account_button()
    create_account_page.open_main_page_recipes()
    login_page.click_login_button_header()
    login_page.set_email(user_name)
    login_page.set_password(user_password)
    login_page.click_login_button()
    # Удаления узера в этом задании нет и возвращать нечего

"""
@pytest.fixture()
def user():
    body = Generatorss.generate_random_payload_for_register_new_user()
    response = requests.post(
                f"{BASE_URL}{API}{USER_URL}register", json=body)
    yield response.json(), response.status_code, body
    requests.delete(f"{BASE_URL}{API}{USER_URL}", headers={
        "Authorization": response.json().get("accessToken")
    })

@pytest.fixture
def authorized_user(main_page, login_page, user,constructor_page):
    main_page.open_main_page_stellarburgers()
    main_page.click_personal_account_button()
    _, _, body = user
    login_page.login(
        email=body.get("email"),
        password=body.get("password"))
    constructor_page.close_modal()
    
@pytest.fixture()
def user_with_order(authorized_user,constructor_page):
    constructor_page.add_buns_to_order()
    constructor_page.click_place_order_button()
    constructor_page.wait_invisible_order_9999()
    constructor_page.close_order_id_popup()
    constructor_page.close_modal()


"""