from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import pytest
import os

@pytest.fixture()
def m_access():
    username="observabilityadmin@gmail.com"
    password="Admin@123"
    location = os.getcwd()
    option=Options()
    option.add_experimental_option("detach",True)
    option.add_argument("--disable-notifications")
    option.add_argument("--allow-running-insecure-content")
    option.add_argument("--disable-web-security")
    prefernces={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    option.add_experimental_option("prefs",prefernces)
    m_access=WebDriver(options=option)
    m_access.get("http://192.168.1.171:8080/mpulseSSO/#/ ")
    m_access.maximize_window()
    m_access.implicitly_wait(10)
    m_access.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
    m_access.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
    m_access.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
    m_access.find_element("xpath",'//*[@ng-reflect-title="MSERVICES"]//div/img').click()

    yield m_access

    m_access.close()





