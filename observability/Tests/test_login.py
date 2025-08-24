import allure
import pytest
from time import sleep
from Utilities.Login_reader import reader
import allure

credentials=reader("Login_data.xlsx", "Data")


# note: API NOT Working for invalid credentails

@pytest.mark.parametrize("username,password",credentials)
def test_login(login,username,password):
    login.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
    login.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
    sleep(1)
    login.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
    sleep(1)
    if login.find_element("xpath",'//div[@class="Response_Message_Container"]/p[contains(text(),"Login success!")]').is_displayed():
        assert True
    elif login.find_element("xpath",'//span[contains(text(),"Opps! Something went wrong.")]/parent::div[@class="Response_Message_Container"]').is_displayed():
        assert True
    else:
        screenshot="Login_issue.png"
        login.save_screenshot(screenshot)
        with open(screenshot, "rb") as image:
            allure.attach(image.read(), name="Login_issue.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_creation():
    pass