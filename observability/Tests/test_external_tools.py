from POM.External_tools import external_tools
import allure

def test_externaltool_basic_auth(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    basic_auth=external_tools(server)
    basic_auth.Basic_auth('Automation Testing','AWS CloudWatch','Testing',
                          'Testing_v1','1.2.3.4','3030','HTTPS','Basic',
                          'mahesh@gmail.co','testcheck','hagen-1','2000')
    if server.find_element('xpath','//div[starts-with(text(),"Success")]').is_displayed():
        assert True
    else:
        screenshot='External_basic_auth_bug.png'
        server.save_screenshot(screenshot)
        with open(screenshot,'rb') as image:
            allure.attach(image.read(), name="External_basic_auth_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_externaltool_auth_API(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    API_auth=external_tools(server)
    API_auth.API_auth('Automation Testing API','Oracle','Staging',
                          'Testing_v1','1.2.3.5','2020','HTTP','API Key',
                          'apikeydummy','Hafen-API','2000')
    if server.find_element('xpath','//div[starts-with(text(),"Success")]').is_displayed():
        assert True
    else:
        screenshot='External_API_auth_bug.png'
        server.save_screenshot(screenshot)
        with open(screenshot,'rb') as image:
            allure.attach(image.read(), name="External_API_auth_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_externaltools_delete(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    Deletion=external_tools(server)
    Deletion.delete('Automation Testing API')
    if server.find_element('xpath','//div[text()="External tool configuration deleted successfully!"]').is_displayed():
        assert True
    else:
        screenshot='External_tool_bug.png'
        server.save_screenshot(screenshot)
        with open(screenshot,'rb') as image:
            allure.attach(image.read(), name="External_tool_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_externaltools_view(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    View=external_tools(server)
    View.view('Production AWS CloudWatch')

