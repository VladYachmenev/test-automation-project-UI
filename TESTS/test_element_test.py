import random
import time

from LOCATOS.elements_filled import TextBoxPage, CheckBoxPage, RadioButtonPage, TablePage, ButtonsPage
from conftest import driver


class TestElements:
    class TestTextElements:
        def test_valid_data(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            full_name, email, current_address, permanent_address = text_page.fill_all()
            text_page.scroll()
            text_page.click_submit()
            output_name, output_email, output_current_address, output_permanent_address = text_page.check_field()
            assert full_name == output_name, 'emaily pizda'
            assert email == output_email, 'occhko'
            assert current_address == output_current_address, 'piza'
            assert permanent_address == output_permanent_address, 'pizza'

        def test_empty_values(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            text_page.scroll()
            text_page.click_submit()
            empty_value = text_page.check_empty_field()
            assert empty_value

        def test_invalid_data(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            text_page.fill_all_invalid()
            text_page.scroll()
            text_page.click_submit()
            empty_value = text_page.check_empty_field()
            assert empty_value == True

    class TestCheckBoxElements:
        def test_checkbox(self, driver):
            checkbox_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            checkbox_page.open()
            checkbox_page.open_all_checkbox_elem()
            checkbox_page.click_checkbox_elem()
            input_list = checkbox_page.check_checkbox_elem()
            output_list = checkbox_page.get_output_result()
            assert input_list == output_list

    class TestRadioButtonElements:
        def test_radiobutton(self, driver):
            radiobutton_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radiobutton_page.open()
            radiobutton_page.click_radiobutton('yes')
            output_yes = radiobutton_page.check_radiobutton()
            radiobutton_page.click_radiobutton('impressive')
            output_impressive = radiobutton_page.check_radiobutton()
            try:
                radiobutton_page.click_radiobutton('no')
            except TypeError:
                print('Button no is not clickable')

            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'

    class TestTable:
        def test_add_person_valid_data(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            input_list = list(table_page.add_new_person())
            output_list = table_page.check_new_person()
            print(input_list)
            print(output_list)
            assert input_list == output_list

        def test_add_person_empty_data(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            table_page.add_new_person_empty_data()
            empty_form = table_page.check_new_person_empty_data()
            assert empty_form

        def test_add_person_invalid_data(self,driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            table_page.add_new_person_invalid_data()
            empty_form = table_page.check_new_person_empty_data()
            assert empty_form

        def test_search_person(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            key_word = list(table_page.add_new_person())[random.randint(1, 4)]
            table_page.search_person(key_word)
            person_list = table_page.check_search_person()
            print(person_list)
            print(key_word)
            assert key_word in person_list

        def test_update_person(self,driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            key = list(table_page.add_new_person())[1]
            table_page.search_person(key)
            first_name = table_page.update_person_info()
            person_list = table_page.check_search_person()
            assert first_name in person_list

        def test_delete_person(self,driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            key = list(table_page.add_new_person())[1]
            table_page.search_person(key)
            table_page.delete_person()
            no_person_list = table_page.check_delete_person()
            assert no_person_list == "No rows found"

    class TestButtons:
        def test_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            buttons_page.click_double_button()
            text_double_button = buttons_page.check_buttons('double_button')
            buttons_page.click_right_button()
            text_right_button = buttons_page.check_buttons('right_button')
            buttons_page.click_me_button()
            text_click_me_button = buttons_page.check_buttons('click_me_button')
            assert text_double_button == "You have done a double click"
            assert text_right_button == "You have done a right click"
            assert text_click_me_button == "You have done a dynamic click"




