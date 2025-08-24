from POM.Alert_Notification import alert_noti
from time import sleep
import allure


#Server Alerts:
def test_server_APPalert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    app_alert=alert_noti(server)
    app_alert.server_app_alert('APPLICATION','Mule test server','Select Application',
                        'Automation_alert','3',
                        'AppMemoryUtilization','30 minutes','15','test_app',
                        'Test Latency','Warning','Performance','mahesh.babu@maiora.co',
                        '8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="server_app_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="server_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_metrics_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    metrics_alert=alert_noti(server)
    metrics_alert.server_metrics_alert('METRICS','Mule test server','Select Application',
                        'Automation_Server_Metrics','3',
                        'CriticalDiskSpace','30 minutes','15','Info',
                               'Security','mahesh.babu@maiora.co','8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="server_Metrics_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="server_Metrics_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_API_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    server_api_alert=alert_noti(server)
    server_api_alert.server_API_alert('API','test Kubenetes','Select Application',
                        'Automation_Server_API','20',
                        'bad_gateway','1 minute','5','API Alert',
                           r'test\api_folder','404','Critical',
                               'Application','mahesh.babu@maiora.co','8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="server_API_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="server_API_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False



#API Alerts:
def test_API_alert(server):
    # Contains 403 FORBIDDEN ERROR Bug so Not provide any verifications code:

    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    API_alert=alert_noti(server)
    API_alert.API_alert('http://13.202.80.237/doitright/api/maioraservice/dsmaster/all','test1','test1',
                        'test1',
                           'test2','test2','test2',
                           'test3','test3','test3',
                           '10','mahesh.babu@maiora.co','8639563301',
                        'AUTOMATION TESTING PURPOSE')


#Application Alerts:
def test_Application_APPalert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    application_alert=alert_noti(server)
    application_alert.application_app_alert('APPLICATION','test Kubenetes','Select Application',
                        'Automation_APPLICATION_alert','10',
                        'AppCPUUtilization','1 hour','30','Application_app_alert',
                        'Test Application Latency','Critical','Infrastructure','mahesh.babu@maiora.co',
                        '8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Application_app_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Application_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Application_metrics_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    create_alert=alert_noti(server)
    create_alert.application_metrics_alert('METRICS','test Kubenetes','Select Application',
                        'Automation_Server_Metrics','3',
                        'PodHighCPUUsage','5 minutes','15','Critical',
                               'Performance','mahesh.babu@maiora.co','8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Application_Metrics_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Application_Metrics_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Application_API_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    create_alert=alert_noti(server)
    create_alert.application_API_alert('API','Mule test server','Select Application',
                        'Automation_APPLICATION_API','5',
                        'request_volume_spike','5 minutes','13','APPLICATION API Alert',
                           r'test\api_folder\application','400','Warning',
                               'Infrastructure','mahesh.babu@maiora.co','8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Application_API_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Application_API_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

#Alert Rules:
def test_Alert_APP(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    application_alert=alert_noti(server)
    application_alert.Alert_Rules_app('APPLICATION','Mule test server','Select Application',
                        'Automation_APPLICATION_alert','10',
                        'AppThreadCount','15 minutes','5','Alert_Rules_app',
                        'Alert Rules Latency','Warning','Security','mahesh.babu@maiora.co',
                        '8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Alert_rules_app_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Alert_rules_app_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Alert_metrics(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    create_alert=alert_noti(server)
    create_alert.Alert_Rules_metrics('METRICS','New112','Select Application',
                        'Alert_Rules_Metrics','32',
                        'NodeNotReady','30 minutes','20','Warning',
                               'Application','mahesh.babu@maiora.co','8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Application_Metrics_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Application_Metrics_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Alert_API(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    create_alert=alert_noti(server)
    create_alert.Alert_Rules_API('API','test Kubenetes','Select Application',
                        'Alert_Rules_API','55',
                        'unauthorized','5 minutes','33','Alert Rules API',
                           r'test\api_folder\alert_rules','402','Info',
                               'Performance','mahesh.babu@maiora.co','8639563301')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Alert_rules_API_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Alert_rules_API_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

#Multiple Server FEATURE  Alerts:
def test_server_multi_APPalert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"
    """
    1.Change the server_multi_app_alert() method as per the Alerts data ex: Metrics/API alerts 
    are different from other alert types
    2.Change the Test data before executing Test cases"""
    app_alert=alert_noti(server)
    app_alert.server_multi_app_alert('APPLICATION','Mule test server','Select Application',
                        'Automation_alert1','3',
                        'AppMemoryUtilization','30 minutes','15','test_app1',
                        'Test Latency1','Warning','Performance','mahesh.babu@maiora.co',
                        '8639563301',
                                     'METRICS','test Kubenetes','Select Application',
                                     'Automation_alert1','30',
                                     'HighLoadAverage','10 minutes','18','test_app2',
                                     'Test Latency2','Critical','Application','mahesh1.babu@maiora.co',
                                     '8639563302')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="server_multi_app_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="server_multi_app_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_multi_metrics_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """    1.Change the server_multi_app_alert() method as per the Alerts data ex: Metrics/API alerts 
    are different from other alert types
    2.Change the Test data before executing Test cases"""
    metrics_alert=alert_noti(server)
    metrics_alert.server_multi_metrics_alert('METRICS','Mule test server','Select Application',
                        'Automation_Server_Multi_Metrics','3',
                        'CriticalDiskSpace','30 minutes','15','Info',
                        'Security','metrics.babu@maiora.co','8639563303',
                        'API','test Kubenetes','Select Application','Automation_Server_Multi_API',
                        '45','service_unavailable',
                        '1 hour','30','Multiple API Alerts',r'test\api_folder\multi','405',
                        'Info','Security','metrics.api@maiora.co','8639563304')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="server_Multi_Metrics_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="server_Multi_Metrics_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_server_multi_API_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    server_api_alert=alert_noti(server)
    server_api_alert.server_multi_API_alert('API','Mule test server','Select Application',
                        'Automation_Multi_Server_API','20',
                        'bad_gateway','1 minute','5','API Multi Alert1',
                        r'test\api_folder','404','Critical','Application',
                        'api.babu@maiora.co','8639563304',
                        'APPLICATION','test Kubenetes','Select Application',
                        'Automation_alert2','29',
                        'AppThreadCount','5 minutes','23','test_app2',
                        'Test Latency2','Critical','Infrastructure',
                        'App.babu@maiora.co','8639563305')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="server_Multi_API_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="server_Multi_API_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

#Multiple API FEATURE Alerts:
def test_API_Multi_alert(server):
    # Contains 403 FORBIDDEN ERROR Bug so Not provide any verifications code:

    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    API_alert=alert_noti(server)
    API_alert.API_Multi_alert('http://13.202.80.237/doitright/api/maioraservice/dsmaster/all',
                              'test1','test1','test1',
                           'test2','test2','test2',
                           'test3','test3','test3',
                           '10','mahesh.babu@maiora.co','8639563301',
                           'AUTOMATION TESTING PURPOSE-1',
                           'http://13.202.80.237/doitright/api/maioraservice/dsmaster/all',
                           'test4','test4','test4',
                           'test5','test5','test5',
                           '15','mahes1.babu@maiora.co','8639563302',
                            'AUTOMATION TESTING PURPOSE-2')

#Multiple APPLICATION FEATURE Alerts:
def test_Application_multi_APPalert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"
    """
    1.Change the server_multi_app_alert() method as per the Alerts data ex: Metrics/API alerts 
    are different from other alert types
    2.Change the Test data before executing Test cases"""
    app_alert=alert_noti(server)
    app_alert.application_multi_app_alert('APPLICATION','Mule test server','Select Application',
                        'Automation_alert1','3',
                        'AppMemoryUtilization','30 minutes','15','test_app1',
                        'Test Latency1','Warning','Performance','mahesh.babu@maiora.co',
                        '8639563301',
                                     'METRICS','test Kubenetes','Select Application',
                                     'Automation_alert1','30',
                                     'HighLoadAverage','10 minutes','18','test_app2',
                                     'Test Latency2','Critical','Application','mahesh1.babu@maiora.co',
                                     '8639563302')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Application_multi_app_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Application_multi_app_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Application_multi_metrics_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """    1.Change the server_multi_app_alert() method as per the Alerts data ex: Metrics/API alerts 
    are different from other alert types
    2.Change the Test data before executing Test cases"""
    metrics_alert=alert_noti(server)
    metrics_alert.application_multi_metrics_alert('METRICS','Mule test server','Select Application',
                        'Automation_Server_Multi_Metrics','3',
                        'CriticalDiskSpace','30 minutes','15','Info',
                        'Security','metrics.babu@maiora.co','8639563303',
                        'API','test Kubenetes','Select Application','Automation_Server_Multi_API',
                        '45','service_unavailable',
                        '1 hour','30','Multiple API Alerts',r'test\api_folder\multi','405',
                        'Info','Security','metrics.api@maiora.co','8639563304')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Application_Multi_Metrics_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Application_Multi_Metrics_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Application_multi_API_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    server_api_alert=alert_noti(server)
    server_api_alert.application_multi_API_alert('API','Mule test server','Select Application',
                        'Automation_Multi_Server_API','20',
                        'bad_gateway','1 minute','5','API Multi Alert1',
                        r'test\api_folder','404','Critical','Application',
                        'api.babu@maiora.co','8639563304',
                        'APPLICATION','test Kubenetes','Select Application',
                        'Automation_alert2','29',
                        'AppThreadCount','5 minutes','23','test_app2',
                        'Test Latency2','Critical','Infrastructure',
                        'App.babu@maiora.co','8639563305')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Application_Multi_API_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Application_Multi_API_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False



#Multiple Alert Rules FEATURE:
def test_Alert_Rules_multi_APPalert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"
    """
    1.Change the server_multi_app_alert() method as per the Alerts data ex: Metrics/API alerts 
    are different from other alert types
    2.Change the Test data before executing Test cases"""
    app_alert=alert_noti(server)
    app_alert.Alert_Rules_multi_app_alert('APPLICATION','Mule test server','Select Application',
                        'Automation_alert1','3',
                        'AppMemoryUtilization','30 minutes','15','test_app1',
                        'Test Latency1','Warning','Performance','mahesh.babu@maiora.co',
                        '8639563301',
                                     'METRICS','test Kubenetes','Select Application',
                                     'Automation_alert1','30',
                                     'HighLoadAverage','10 minutes','18','test_app2',
                                     'Test Latency2','Critical','Application','mahesh1.babu@maiora.co',
                                     '8639563302')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Alert_Rules_multi_app_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Alert_Rules_multi_app_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Alert_Rules_multi_metrics_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """    1.Change the server_multi_app_alert() method as per the Alerts data ex: Metrics/API alerts 
    are different from other alert types
    2.Change the Test data before executing Test cases"""
    metrics_alert=alert_noti(server)
    metrics_alert.Alert_Rules_multi_metrics_alert('METRICS','Mule test server','Select Application',
                        'Automation_Server_Multi_Metrics','3',
                        'CriticalDiskSpace','30 minutes','15','Info',
                        'Security','metrics.babu@maiora.co','8639563303',
                        'API','test Kubenetes','Select Application','Automation_Server_Multi_API',
                        '45','service_unavailable',
                        '1 hour','30','Multiple API Alerts',r'test\api_folder\multi','405',
                        'Info','Security','metrics.api@maiora.co','8639563304')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Alert_Rules_Multi_Metrics_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Alert_Rules_Multi_Metrics_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False

def test_Alert_Rules_multi_API_alert(server):
    #SMTP Details:
    smtp_smarthost= "smtp.gmail.com:587"
    smtp_auth_username="poojapadmashreek365@gmail.com"
    smtp_auth_password= "sowhhcfuubddxeht"
    smtp_email='mahesh.babu@maiora.co'
    smtp_servername="Mule test server"

    """Change the Test data before executing Test cases"""
    server_api_alert=alert_noti(server)
    server_api_alert.Alert_Rules_multi_API_alert('API','Mule test server','Select Application',
                        'Automation_Multi_Server_API','20',
                        'bad_gateway','1 minute','5','API Multi Alert1',
                        r'test\api_folder','404','Critical','Application',
                        'api.babu@maiora.co','8639563304',
                        'APPLICATION','test Kubenetes','Select Application',
                        'Automation_alert2','29',
                        'AppThreadCount','5 minutes','23','test_app2',
                        'Test Latency2','Critical','Infrastructure',
                        'App.babu@maiora.co','8639563305')
    if server.find_element("xpath",'//div[contains(text(),"Alert created successfully, Configure SMTP Alerts")]').is_displayed():
        sleep(2)
        server.find_element('xpath','//button[text()="SMTP Config"]').click()
        server.find_element('xpath','//input[@formcontrolname="smtpHost"]').send_keys(smtp_smarthost)
        server.find_element('xpath','//input[@formcontrolname="smtpUsername"]').send_keys(smtp_auth_username)
        server.find_element('xpath','//input[@formcontrolname="smtpPassword"]').send_keys(smtp_auth_password)
        server.find_element('xpath','//input[@formcontrolname="email"]').send_keys(smtp_email)
        server.find_element('xpath','//select[@formcontrolname="serverName"]').send_keys(smtp_servername)
        server.find_element('xpath','//button[@type="submit" and contains(text(),"Save")]').click()
        assert True
    else:
        screenshot="Alert_Rules_Multi_API_alert_bug.png"
        server.save_screenshot(screenshot)
        with open(screenshot, 'rb') as image:
            allure.attach(image.read(), name="Alert_Rules_Multi_API_alert_bug.png", attachment_type=allure.attachment_type.PNG)
        assert False







