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


class CheckBoxPageLocators:
    BUTTON_OPEN_ALL = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    CHECKBOX_LIST = (By.CSS_SELECTOR, 'span.rct-title')
    СHECKED_LIST = (By.CSS_SELECTOR, 'svg.rct-icon-check')
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_LIST = (By.CSS_SELECTOR, 'span.text-success')


class RadioButtonPageLocators:
    BUTT0N_YES = (By.CSS_SELECTOR, 'div[class^="custom"] [for="yesRadio"]')
    BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, 'div[class^="custom"] [for="impressiveRadio"]')
    BUTTON_N0 = (By.CSS_SELECTOR, 'div[class^="custom"] [for="noRadio"]')
    OUTPUT_RADIOBUTTON = (By.CSS_SELECTOR,'span.text-success')




