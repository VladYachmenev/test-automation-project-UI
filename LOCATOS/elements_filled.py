import base64
import os
import imghdr
import allure
import requests
from LOCATOS.element_locators import TextBoxLocators, CheckBoxPageLocators, RadioButtonPageLocators, TablePageLocators, \
    ButtonsPageLocators, LinksPageLocators, UploadDownloadLocators, DynamicPropertiesLocators
from PAGES.base_page import BasePage
import time
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_person2, generated_new_person, generate_file
import random


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    @allure.step("Fill valid data in all fields")
    def fill_all(self):
        person_information = next(generated_person())
        full_name = person_information.full_name
        email = person_information.email
        current_address = person_information.current_address
        permanent_address = person_information.permanent_address
        with allure.step('fill fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return full_name, email, current_address, permanent_address

    @allure.step("Fill invalid data in all fields")
    def fill_all_invalid(self):
        person_information = next(generated_person2())
        full_name = person_information.full_name
        email = person_information.email
        current_address = person_information.current_address
        permanent_address = person_information.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return full_name, email, current_address, permanent_address

    @allure.step("Click submit")
    def click_submit(self):
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(15)

    @allure.step("Scroll to element")
    def scroll(self):
        self.scroll_with_pixiles()

    @allure.step("Check field")
    def check_field(self):
        full_name = self.element_is_visible(self.locators.CREATED_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

    @allure.step("Check field")
    def check_empty_field(self):
        empty_name = self.elements_is_not_visible(self.locators.CREATED_NAME)
        return empty_name


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step("Click button")
    def open_all_checkbox_elem(self):
        self.element_is_visible(self.locators.BUTTON_OPEN_ALL).click()

    @allure.step("Random click checkboxes")
    def click_checkbox_elem(self):
        list_checkbox = self.elements_are_visible(self.locators.CHECKBOX_LIST)
        count = 25
        while count != 0:
            item = list_checkbox[random.randint(1, 16)]
            if count > 0:
                self.scroll_to_go_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step("Check text checkboxes")
    def check_checkbox_elem(self):
        checked_list = self.elements_are_present(self.locators.СHECKED_LIST)
        data = []
        for elem in checked_list:
            text_item = elem.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(text_item.text.lower().replace(' ', '').replace('doc', '').replace('.', ''))

        return data

    def get_output_result(self):
        output_list = self.elements_are_present(self.locators.OUTPUT_LIST)
        data = []
        for elem in output_list:
            data.append(elem.text.replace(' ', '').lower())
        return data


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("Click radiobuttons")
    def click_radiobutton(self, value):
        dict_radiobutton = {'yes': self.locators.BUTT0N_YES,
                            'impressive': self.locators.BUTTON_IMPRESSIVE,
                            'no': self.locators}
        self.element_is_visible(dict_radiobutton[value]).click()

    @allure.step("Check radiobuttons text")
    def check_radiobutton(self):
        output_value = self.element_is_visible(self.locators.OUTPUT_RADIOBUTTON).text
        return output_value


class TablePage(BasePage):
    locators = TablePageLocators()

    @allure.step("Click button to add person")
    def click_button_add(self):
        self.element_is_visible(self.locators.BUTTON_ADD).click()

    @allure.step("Fill valid data in all fields")
    def add_new_person(self):
        person_info = next(generated_new_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        with allure.step("filling fields"):
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTAMENT_INPUT).send_keys(department)
        with allure.step("click submit"):
            self.element_is_visible(self.locators.BUTTON_SUBMIT).click()
        return first_name, last_name, str(age), email, str(salary), department

    @allure.step("Check new person info in table")
    def check_new_person(self):
        all_data = self.elements_are_present(self.locators.ALL_DATA)
        list_data = []
        for elem in all_data:
            list_data.append(elem.text)
        list_data.pop(-1)
        return list_data

    @allure.step("Click submit without data")
    def add_new_person_empty_data(self):
        self.element_is_clickable(self.locators.BUTTON_SUBMIT).click()

    @allure.step("Check,that the user has not been created")
    def check_new_person_empty_data(self):
        if self.element_is_present(self.locators.USER_NOT_VALIDATED_FORM):
            return True

    @allure.step("Fill invalid data in all fields")
    def add_new_person_invalid_data(self):
        person_info = next(generated_new_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.invalid_email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        with allure.step("filling fields"):
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTAMENT_INPUT).send_keys(department)
        with allure.step("click submit"):
            self.element_is_visible(self.locators.BUTTON_SUBMIT).click()

    @allure.step("Search new person")
    def search_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    @allure.step("Clear search person input")
    def clear_search_person(self):
        self.element_is_visible(self.locators.SEARCH_INPUT).clear()

    @allure.step("Check,that the correct person was found")
    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        person_info = delete_button.find_element(By.XPATH, self.locators.USER_DATA)
        return person_info.text.splitlines()
    @allure.step("Update new person info")
    def update_person_info(self):
        person_info = next(generated_new_person())
        first_name = person_info.first_name
        with allure.step('click button update'):
            self.element_is_visible(self.locators.BUTTON_UPDATE).click()
        with allure.step('clear first name field'):
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).clear()
        with allure.step('fill first name'):
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
        with allure.step('click submit'):
            self.element_is_visible(self.locators.BUTTON_SUBMIT).click()
        return first_name

    @allure.step("Click on the delete button")
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step("Check,that person has been deleted")
    def check_delete_person(self):
        return self.element_is_visible(self.locators.NO_USERS).text


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("Double click on the button")
    def click_double_button(self):
        self.double_click(self.element_is_visible(self.locators.BUTTON_DOUBLE_CLICK))

    @allure.step("Right click on the button")
    def click_right_button(self):
        self.right_click(self.element_is_visible(self.locators.BUTTON_RIGHT_CLICK))

    @allure.step("Click on the button")
    def click_me_button(self):
        self.element_is_visible(self.locators.BUTTON_CLICK_ME).click()

    @allure.step("Check,that the text matches the button pressed")
    def check_buttons(self, button):
        if button == 'double_button':
            return self.element_is_present(self.locators.SUCCESS_DOUBLE_CLICK).text
        if button == 'right_button':
            return self.element_is_present(self.locators.SUCCESS_RIGHT_CLICK).text
        if button == 'click_me_button':
            return self.element_is_present(self.locators.SUCCESS_CLICK_ME).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step("Check simple link")
    def check_new_tab_link(self):
        simple_link = self.element_is_visible(self.locators.NEW_TAB_LINK)
        link = simple_link.get_attribute('href')
        request = requests.get(link)
        if request.status_code == 200:
            simple_link.click()
            self.switch_new_tab()
            current_link_new_tab = self.driver.current_url
            return link, current_link_new_tab
        else:
            print("Invalid link")

    @allure.step("Check status code of api call links")
    def check_api_call_links(self, link_name):
        with allure.step('Send get request'):
            request = requests.get(f"https://demoqa.com/{link_name}")
        return request.status_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadLocators()

    @allure.step("Upload new file")
    def upload_new_file(self):
        file, path = generate_file()
        with allure.step("upload file"):
            self.element_is_visible(self.locators.SELECT_FILE_BUTTON).send_keys(file)
            os.remove(file)
        with allure.step("check file text"):
            path_text = self.element_is_present(self.locators.FILE_PATH_TEXT).text
        return path_text.split('\\')[-1], path.split('\\')[-1]

    @allure.step("Download file")
    def download_file(self):
        link = self.element_is_visible(self.locators.FILE_DOWNLOAD_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\yachm\OneDrive\Рабочий стол\ТЕСТИРОВКА\ТЕОРИЯ\file{random.randint(0, 90)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.abspath(path_name_file)
            f.close()
        return check_file

    @allure.step("Check, that file has right format")
    def check_download_file(self, filename):
        fd = open(filename, 'rb').read()
        return imghdr.what(None, fd)


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    @allure.step("Check, that button is clickable after 5 second")
    def check_button_will_enable(self):
        if self.element_is_clickable(self.locators.BUTTON_WILL_ENABLE):
            return True

    @allure.step("Check, that button is visible after 5 second")
    def check_button_visible_after(self):
        if self.element_is_visible(self.locators.BUTTON_VISIBLE_AFTER):
            return True
