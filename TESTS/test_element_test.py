import time
from LOCATOS.elements_filled import TextBoxPage
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

            time.sleep(10)

        def test_empty_values(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            text_page.scroll()
            text_page.click_submit()
            empty_name = text_page.check_empty_field()
            assert empty_name == True
            time.sleep(10)


        def test_invalid_data(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            text_page.fill_all_invalid()
            text_page.scroll()
            text_page.click_submit()
            empty_value = text_page.check_empty_field()
            assert empty_value  == True
            time.sleep(10)
