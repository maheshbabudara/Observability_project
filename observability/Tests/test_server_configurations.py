from time import sleep

from POM.server_configuration import server_configuration
import allure


#CREATION OF SERVERS:
def test_server_creation_docker(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_docker=server_configuration(server)
    server_docker.docker('Docker creation','2.11.3.1','8080','Windows',
                         'Admin','8639563301','docker_check','2.11.3.2',
                         '2030','Dock/new/check','docker-create',
                         'Automation Testing purpose','Hafen',
                         'Hafen-docker','1234567')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="Docker creation":
        assert True
    else:
        screenshot="docker_creation_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="docker_creation_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_creation_kubernetes(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_kubernetes=server_configuration(server)
    server_kubernetes.kubernetes('Kubernetes creation','2.11.3.1','8080','Windows',
                         'User','8639563301','Kubernetes_check','2.11.3.2',
                         '2030','Kubernetes/new/check','Kubernetes-create',
                         'Automation Testing purpose','Hafen',
                         'Hafen-Kubernetes','1234567')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    sleep(3)
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="Kubernetes creation":
        assert True
    else:
        screenshot="Kubernetes_creation_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Kubernetes_creation_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_creation_Baremetal(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_Baremetal=server_configuration(server)
    server_Baremetal.Baremetal('Baremetal creation','2.11.3.1','8080','Windows',
                         'User','8639563301','Baremetal_check','2.11.3.2',
                         '2030','Baremetal/new/check','Baremetal-create',
                         'Automation Testing purpose','Hafen')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    sleep(3)
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="Baremetal creation":
        assert True
    else:
        screenshot="Baremetal_creation_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Baremetal_creation_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_creation_all_types(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_all_types=server_configuration(server)
    server_all_types.all_types('docker_kuber_bare creation','2.11.3.1','8080',
                            'Windows','abc','8639563301','docker_kuber_bare_check',
                            '2.11.3.2','2030','docker_kuber_bare/new/check',
                            'docker_kuber_bare-create','Automation Testing purpose',
                            'Hafen','Hafen-docker','221133',
                            'Hafen-Kubernetes','234561')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    sleep(3)
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="docker_kuber_bare creation":
        assert True
    else:
        screenshot="docker_kuber_bare_creation_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="docker_kuber_bare_creation_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False


#Edit of servers:
def test_server_edit_docker(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_docker_edit=server_configuration(server)
    server_docker_edit.docker_edit('Docker Edit','test kube','2.12.3.0','8080','Windows',
                         'Admin','8639563301','Docker Edit_check','2.12.3.0',
                         '2030','Docker Edit/new/check','Docker Edit',
                         'Automation Testing purpose','Hafen',
                         'Hafen-docker','1234567',
                                   'changed to Kubernetes','1234567')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="test kube":
        assert True
    else:
        screenshot="Docker_Edit_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Docker_Edit_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_edit_kubernetes(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_kubernetes_edit=server_configuration(server)
    server_kubernetes_edit.kubernetes_edit('test kube','Kubernetes Edit','2.11.3.1','8080','Windows',
                         'User','8639563301','Kubernetes_Edit_check','2.11.3.2',
                         '2030','Kubernetes_edit/new/check','Kubernetes-create',
                         'Automation Testing purpose','Hafen',
                         'Hafen-Kubernetes_Edit','1234567',
                        'changed to Docker','22113344')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    sleep(3)
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="Kubernetes Edit":
        assert True
    else:
        screenshot="Kubernetes_Edit_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Kubernetes_Edit_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_edit_Baremetal(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_Baremetal_edit=server_configuration(server)
    server_Baremetal_edit.Baremetal_edit('Kubernetes Edit','Baremetal edit','2.11.3.1','8080','Windows',
                         'User','8639563301','Baremetal_edit','2.11.3.2',
                         '2030','Baremetal_edit/new/check','Baremetal-create',
                         'Changing to Barmetal from docker & kubernetes','Hafen',
                        'Hafen-Kubernetes_Edit','1234567',
                        'changed to Barmetal','22113344')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    sleep(3)
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="Baremetal edit":
        assert True
    else:
        screenshot="Baremetal_edit_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Baremetal_edit_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_delete(server):
    """
    Change the Test Data before executing Test cases
    :param server:
    :return:
    """
    server_delete=server_configuration(server)
    server_delete.delete_server('docker_kuber_bare creation')
    # search=server.find_element("xpath",'//input[@placeholder="Search"]')
    # search.send_keys('Docker creation')
    # search.click()
    sleep(3)
    if server.find_element('xpath','//tr[@class="ng-star-inserted"][1]//a').text.strip()=="docker_kuber_bare creation":
        assert True
    else:
        screenshot="docker_kuber_bare_creation_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="docker_kuber_bare_creation_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False



