from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locators, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locators))

    def elements_are_visible(self, locators, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locators))

    def element_is_clickable(self, locators, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locators))

    def element_is_present(self, locators, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locators))

    def elements_are_present(self, locators, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locators))

    def elements_is_not_visible(self, locators, timeout=5):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locators))

    def scroll_to_go_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_with_pixiles(self):
        return self.driver.execute_script("window.scrollBy(0, 400);")

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
