from selenium.webdriver.common.by import By

class CreateRecipePageLocators:
    RECIPE_NAME_FIELD = (By.CLASS_NAME, 'styles_inputField__3eqTj')
    INGREDIENTS_FIELD = (By.CSS_SELECTOR, ".styles_ingredientsInput__1zzql")
    INGREDIENTS_AMOUNT_FIELD =  (By.CSS_SELECTOR ,".styles_ingredientsAmountValue__2matT")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    COOCING_TIME_FIELD =  (By.XPATH, "//div[text()='Время приготовления']/following-sibling::input") 
    RECIPE_DESCRIPTION_FILD = (By.CSS_SELECTOR, ".styles_textareaField__1wfhC")
    ADD_PHOTO_BUTTON = (By.XPATH, "//div[text()='Выбрать файл']")
    CREATE_RECIPE_BUTTON_HEADER = (By.XPATH, "//a[text()='Создать рецепт']")
    CREATED_RECIPE_NAME = (By.CSS_SELECTOR, ".styles_single-card__title__2QMPq")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    UPLOAD_RECIPE_IMAGE = (By.CSS_SELECTOR, ".styles_fileInput__3HjP3")
    FIRST_INGREDIENT = (By.XPATH, "//div[text()='индейка']")
    RECIPE_NAME_AFTER_CREAT_RECIPE = (By.CSS_SELECTOR, ".styles_single-card__title__2QMPq")
