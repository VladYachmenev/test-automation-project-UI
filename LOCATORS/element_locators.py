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
    OUTPUT_RADIOBUTTON = (By.CSS_SELECTOR, 'span.text-success')


class TablePageLocators:
    # add person
    BUTTON_ADD = (By.CSS_SELECTOR, 'button#addNewRecordButton')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input#firstName')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, 'input#age')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input#salary')
    DEPARTAMENT_INPUT = (By.CSS_SELECTOR, 'input#department')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button#submit')
    ALL_DATA = (By.XPATH, '//div[@class="rt-tbody"]/div[4]//div[@class="rt-td"]')

    USER_NOT_VALIDATED_FORM = (By.CSS_SELECTOR, 'form.was-validated')
    # search person
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input#searchBox')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    USER_DATA = ".//ancestor::div[@class='rt-tr-group']"

    # update person info
    BUTTON_UPDATE = (By.CSS_SELECTOR, 'span[title="Edit"]')

    # delete person
    NO_USERS = (By.CSS_SELECTOR, 'div.rt-noData')


class ButtonsPageLocators:
    BUTTON_DOUBLE_CLICK = (By.CSS_SELECTOR, 'button#doubleClickBtn')
    BUTTON_RIGHT_CLICK = (By.CSS_SELECTOR, 'button#rightClickBtn')
    BUTTON_CLICK_ME = (By.XPATH, './/div[3]/button')

    SUCCESS_DOUBLE_CLICK = (By.CSS_SELECTOR, 'p#doubleClickMessage')
    SUCCESS_RIGHT_CLICK = (By.CSS_SELECTOR, 'p#rightClickMessage')
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, 'p#dynamicClickMessage')


class LinksPageLocators:
    NEW_TAB_LINK = (By.CSS_SELECTOR, 'a#simpleLink')

    # api call links
    CREATED_LINK = (By.CSS_SELECTOR, 'a#created')
    NO_CONTENT_LINK = (By.CSS_SELECTOR, 'a#no-content')
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, 'a#unauthorized')


class UploadDownloadLocators:
    SELECT_FILE_BUTTON = (By.CSS_SELECTOR, 'input#uploadFile')
    FILE_PATH_TEXT = (By.CSS_SELECTOR, 'p#uploadedFilePath')
    FILE_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a#downloadButton')


class DynamicPropertiesLocators:
    BUTTON_WILL_ENABLE = (By.CSS_SELECTOR, 'button#enableAfter')
    BUTTON_VISIBLE_AFTER = (By.CSS_SELECTOR, 'button#visibleAfter')




