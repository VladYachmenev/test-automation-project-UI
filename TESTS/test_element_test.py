from LOCATOS.elements_filled import TextBoxPage, CheckBoxPage, RadioButtonPage
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
            assert empty_value == True

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
