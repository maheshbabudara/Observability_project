from time import sleep
from Ms_Access.POM_MS_ACCESS.users import users
import allure

def test_user_creation(m_access):
    """
    Change the Test Data before executing the Test case
    :param m_access:
    :return:
    """
    create_user=users(m_access)
    create_user.creation("Automation","Test","mahesh babu test","test@123",
                         "Automation Testing purpose","mahesh.babu1@maiora.co",
                         "OBSERVABILITY","check) ' WAITFOR DELAY '0:0:15' --")

    if m_access.find_element("xpath",'//span[text()="Success"]').is_displayed():
        assert True
    else:
        screenshot="user_creation_bug.png"
        m_access.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="user_creation_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False
def test_user_creation_duplicate(m_access):
    """
    Change the Test Data before executing the Test case
    :param m_access:
    :return:
    """
    duplicate_user=users(m_access)
    duplicate_user.duplicate("Automation","Test","mahesh babu test","test@123",
                         "Automation Testing purpose","mahesh.babu1@maiora.co",
                         "OBSERVABILITY","check) ' WAITFOR DELAY '0:0:15' --")

    if m_access.find_element("xpath",'//span[text()="The email ID provided is already associated with another user" or text()="The user name provided is already associated with another user"]').is_displayed():
        assert True
    else:
        screenshot="duplicate_user_bug.png"
        m_access.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="duplicate_user_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_user_edit(m_access):
    """
    Change the Test Data before executing the Test case
    :param m_access:
    :return:
    """
    edit_user=users(m_access)
    edit_user.edit("edit_mahesh babu","edit_Automation","edit_Test","edit_mahesh babu 12",
                         "edit Automation Testing purpose","mahesh.babu5@maiora.co",
                         "MSERVICES","check) ' WAITFOR DELAY '0:0:15' --")

    if m_access.find_element("xpath",'//span[text()="Success"]').is_displayed():
        assert True
    else:
        screenshot="edit_user_bug.png"
        m_access.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="edit_user_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_user_edit_permission(m_access):
    """
    Change the Test Data before executing the Test case
    :param m_access:
    :return:
    """
    edit_permission=users(m_access)
    edit_permission.edit_permissions("edit_mahesh babu 12")

    if m_access.find_element("xpath",'//span[text()="Success"]').is_displayed():
        assert True
    else:
        screenshot="edit_permission_user_bug.png"
        m_access.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="edit_permission_user_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False