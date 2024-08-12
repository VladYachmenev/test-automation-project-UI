from selenium.webdriver.common.by import By


class TextBoxLocators:
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea#permanentAddress')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    CREATED_NAME = (By.CSS_SELECTOR, 'p#name')
    CREATED_EMAIL = (By.CSS_SELECTOR, 'p#email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p#currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p#permanentAddress')
