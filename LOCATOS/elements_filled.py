from LOCATOS.element_locators import TextBoxLocators, CheckBoxPageLocators, RadioButtonPageLocators
from PAGES.base_page import BasePage
import time
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_person2
import random


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_all(self):
        person_information = next(generated_person())
        full_name = person_information.full_name
        email = person_information.email
        current_address = person_information.current_address
        permanent_address = person_information.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return full_name, email, current_address, permanent_address

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

    def click_submit(self):
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(15)

    def scroll(self):
        self.scroll_with_pixiles()

    def check_field(self):
        full_name = self.element_is_visible(self.locators.CREATED_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

    def check_empty_field(self):
        empty_name = self.elements_is_not_visible(self.locators.CREATED_NAME)
        return empty_name


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_all_checkbox_elem(self):
        self.element_is_visible(self.locators.BUTTON_OPEN_ALL).click()

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

    def click_radiobutton(self, value):
        dict_radiobutton = {'yes': self.locators.BUTT0N_YES,
                            'impressive': self.locators.BUTTON_IMPRESSIVE,
                            'no': self.locators}
        self.element_is_visible(dict_radiobutton[value]).click()

    def check_radiobutton(self):
        output_value = self.element_is_visible(self.locators.OUTPUT_RADIOBUTTON).text
        return output_value












