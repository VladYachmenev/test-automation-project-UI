import random
from LOCATORS.elements_filled import TextBoxPage, CheckBoxPage, RadioButtonPage, TablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage
from conftest import driver
import allure


@allure.suite('Elements')
class TestElements:
    @allure.feature('TextElements')
    class TestTextElements:
        @allure.title('Add person with valid data')
        def test_valid_data(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            full_name, email, current_address, permanent_address = text_page.fill_all()
            text_page.scroll()
            text_page.click_submit()
            output_name, output_email, output_current_address, output_permanent_address = text_page.check_field()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_current_address
            assert permanent_address == output_permanent_address

        @allure.title('Add person with empty data')
        def test_empty_values(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            text_page.scroll()
            text_page.click_submit()
            empty_value = text_page.check_empty_field()
            assert empty_value

        @allure.title('Add person with invalid data')
        def test_invalid_data(self, driver):
            text_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_page.open()
            text_page.fill_all_invalid()
            text_page.scroll()
            text_page.click_submit()
            empty_value = text_page.check_empty_field()
            assert empty_value

    @allure.feature('CheckBox')
    class TestCheckBoxElements:
        @allure.title('Check all checkboxes')
        def test_checkbox(self, driver):
            checkbox_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            checkbox_page.open()
            checkbox_page.open_all_checkbox_elem()
            checkbox_page.click_checkbox_elem()
            input_list = checkbox_page.check_checkbox_elem()
            output_list = checkbox_page.get_output_result()
            assert input_list == output_list

    @allure.feature('RadioButton')
    class TestRadioButtonElements:
        @allure.title('Check all radiobuttons')
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

    @allure.feature('Table')
    class TestTable:
        @allure.title('Add new person in table with valid data')
        def test_add_person_valid_data(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            input_list = list(table_page.add_new_person())
            output_list = table_page.check_new_person()
            assert input_list == output_list

        @allure.title('Add person in table with empty data')
        def test_add_person_empty_data(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            table_page.add_new_person_empty_data()
            empty_form = table_page.check_new_person_empty_data()
            assert empty_form

        @allure.title('Add person in table with invalid data')
        def test_add_person_invalid_data(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            table_page.add_new_person_invalid_data()
            empty_form = table_page.check_new_person_empty_data()
            assert empty_form

        @allure.title('Add new person and search person')
        def test_search_person(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            key_word = list(table_page.add_new_person())[random.randint(1, 4)]
            table_page.search_person(key_word)
            person_list = table_page.check_search_person()
            assert key_word in person_list

        @allure.title('Add new person in table and update person info')
        def test_update_person(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            key = list(table_page.add_new_person())[1]
            table_page.search_person(key)
            first_name = table_page.update_person_info()
            person_list = table_page.check_search_person()
            assert first_name in person_list

        @allure.title('Add new person in table and delete person ')
        def test_delete_person(self, driver):
            table_page = TablePage(driver, 'https://demoqa.com/webtables')
            table_page.open()
            table_page.click_button_add()
            key = list(table_page.add_new_person())[1]
            table_page.search_person(key)
            table_page.delete_person()
            no_person_list = table_page.check_delete_person()
            assert no_person_list == "No rows found"

    @allure.feature('Buttons')
    class TestButtons:
        @allure.title('Check all buttons')
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

    @allure.feature('Links')
    class TestLinks:
        @allure.title('Check simple link')
        def test_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            new_tab_link, current_link = links_page.check_new_tab_link()
            assert new_tab_link == current_link, 'Link is broken'

        @allure.title('Check api call links')
        def test_api_call_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            created_link_status_code = links_page.check_api_call_links('created')
            no_content_link = links_page.check_api_call_links('no-content')
            unauthorized_link = links_page.check_api_call_links('unauthorized')
            moved_link = links_page.check_api_call_links('moved')
            bad_request_link = links_page.check_api_call_links('bad-request')
            forbidden_link = links_page.check_api_call_links('forbidden')
            not_found_link = links_page.check_api_call_links('invalid-url')
            assert created_link_status_code == 201, 'inappropriate status code'
            assert no_content_link == 204, 'inappropriate status code'
            assert unauthorized_link == 401, 'inappropriate status code'
            assert moved_link == 301, 'inappropriate status code'
            assert bad_request_link == 400, 'inappropriate status code'
            assert forbidden_link == 403, 'inappropriate status code'
            assert not_found_link == 404, 'inappropriate status code'

    @allure.feature('Upload and Download')
    class TestUploadDownload:
        @allure.title('Check upload file')
        def test_upload_file(self, driver):
            download_upload_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_upload_page.open()
            file_path, path_text_result = download_upload_page.upload_new_file()
            assert file_path == path_text_result, 'file not loaded'

        @allure.title('Check download file')
        def test_download_file(self, driver):
            download_page_upload_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page_upload_page.open()
            file_name = download_page_upload_page.download_file()
            file_format = download_page_upload_page.check_download_file(file_name)
            assert file_format == 'jpeg', 'file failed to download'

    @allure.feature('DynamicProperties')
    class TestDynamicProperties:
        @allure.title('Check button, which will clickable after 5 seconds')
        def test_button_will_enable(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            check_button = dynamic_properties_page.check_button_will_enable()
            assert check_button is True

        @allure.title('Check button, which will visible after 5 seconds')
        def test_button_visible_after(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            check_button = dynamic_properties_page.check_button_visible_after()
            assert check_button is True
