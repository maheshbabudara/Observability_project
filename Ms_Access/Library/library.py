from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys


class Base:
    def __init__(self,driver):
        self.driver=driver
        self.action=ActionChains(self.driver)

    #Generic methods:
    def search_element(self,locator):
        """Finding Unique web element"""
        element=WebDriverWait(self.driver, 10, poll_frequency=0.5, ignored_exceptions=[
            ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException,Exception
        ]).until(e.visibility_of_element_located(locator))
        # element=self.driver.find_element(*locator)
        return element
    def search_elements(self,locator):
        """Finding List of web elements"""
        elements=WebDriverWait(self.driver, 10, poll_frequency=0.5, ignored_exceptions=[
            NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,Exception
        ]).until(e.visibility_of_all_elements_located(locator))
        # elements=self.driver.find_elements(*locator)
        return elements
    def send_data(self,locator,data):
        """Sending a data to an element"""
        web_element=self.search_element(locator)
        web_element.send_keys(data)
    def click(self,locator):
        """Click an element"""
        web_element=self.search_element(locator)
        web_element.click()
    def dynamic_click(self,locator):
        """Using Javascript method click an element"""
        web_element=self.search_element(locator)
        self.driver.execute_script("arguments[0].click();",web_element)
    def scroll(self,locator):
        """Scroll to respective element"""
        web_element=self.search_element(locator)
        self.action.scroll_to_element(web_element).perform()
    def zoom(self, zoom=80):
        self.driver.execute_script(f'document.body.style.zoom="{zoom}%"')

    def clear(self,locator):
        element=self.search_element(locator)
        element.clear()

    #Ms Access Methods:
    def select_applications(self,locator,app):
        applications=self.search_elements(locator)
        for application in applications:
            if application.text==app:
                application.click()
                break
    def select_roles(self,locator,role):
        roles=self.search_elements(locator)
        for rol in roles:
            if rol.text==role:
                rol.click()
                break






