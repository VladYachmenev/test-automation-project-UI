from LOCATOS.element_locators import TextBoxLocators
from PAGES.base_page import BasePage
import time

from generator.generator import generated_person, generated_person2


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
        return full_name, email , current_address, permanent_address


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





