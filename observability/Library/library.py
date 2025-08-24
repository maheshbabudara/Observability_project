
from selenium.webdriver.chrome.webdriver import WebDriver as chromedriver
from selenium.webdriver.edge.webdriver import WebDriver as edgedriver
from selenium.webdriver.firefox.webdriver import WebDriver as firefoxdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains,Keys

class Base:
    def __init__(self,driver):
        self.driver=driver
        self.action=ActionChains(self.driver)

    #Generic Methods:
    def search_element(self,locator):
        web_element=self.driver.find_element(*locator)
        return web_element

    def search_elements(self,locator):
        web_elements=self.driver.find_elements(*locator)
        return web_elements

    def click(self,locator):
        element=self.search_element(locator)
        element.click()

    def dynamic_click(self,locator):
        element=self.search_element(locator)
        self.driver.execute_script('arguments[0].click();',element)

    def send_data(self,locator,test_data):
        element=self.search_element(locator)
        element.send_keys(test_data)

    def clear(self,locator):
        element=self.search_element(locator)
        element.clear()

    def zoomout(self,size=80):
        self.driver.execute_script(f"document.body.style.zoom='{int(size)}%'")
        # self.driver.execute_script(f"document.body.style.zoom='{int(size)}%'")
    def scroll(self,locator):
        element=self.search_element(locator)
        self.action.scroll_to_element(element).perform()

    #Server Monitoring:
    def server_selection(self,locator,test_server):
        element=Select(self.search_element(locator))
        element.select_by_visible_text(test_server)
        # element.select_by_value("2")

    #Global Config:
    def alert_select(self,locator,alert_type):
        alert=Select(self.search_element(locator))
        alert.select_by_visible_text(alert_type)

    def metrics_name(self,locator,metrics):
        metric=Select(self.search_element(locator))
        metric.select_by_visible_text(metrics)

    def alert_severity(self,locator,severity):
        sev=Select(self.search_element(locator))
        sev.select_by_visible_text(severity)

    def alert_category(self,locator,alert_category):
        cate=Select(self.search_element(locator))
        cate.select_by_visible_text(alert_category)
    def eval_period(self,locator,evalution_period):
        period=Select(self.search_element(locator))
        period.select_by_visible_text(evalution_period)

    def server_select(self,locator,sever):
        serv=Select(self.search_element(locator))
        serv.select_by_visible_text(sever)

    def global_config_click(self,locator):
        create_btn=self.search_element(locator)
        self.driver.execute_script('arguments[0].click();',create_btn)

    def API_name(self,locator,api):
        api_value= Select(self.search_element(locator))
        api_value.select_by_visible_text(api)

    def Application(self,locator,app):
        application_value= Select(self.search_element(locator))
        application_value.select_by_visible_text(app)

    #Log Management Methods:
    def log_server(self,locator,server):
        server_value=Select(self.search_element(locator))
        server_value.select_by_visible_text(server)

    def log_timerange(self,locator,time_range):
        range=Select(self.search_element(locator))
        range.select_by_visible_text(time_range)

    def log_level(self,locator,levels):
        level_value=Select(self.search_element(locator))
        level_value.select_by_visible_text(levels)

    def log_source(self,locator,source):
        source_value=Select(self.search_element(locator))
        source_value.select_by_visible_text(source)

    #Alert_Notifications:
    def alert_notifi_type(self,locator,type):
        types=Select(self.search_element(locator))
        types.select_by_visible_text(type)

    def alert_notifi_server(self,locator,server):
        servers=Select(self.search_element(locator))
        servers.select_by_visible_text(server)

    def alert_notifi_app(self,locator,app):
        apps=Select(self.search_element(locator))
        apps.select_by_visible_text(app)

    def alert_notifi_propertyname(self,locator,propertyname):
        propertynames=Select(self.search_element(locator))
        propertynames.select_by_visible_text(propertyname)

    def alert_evalution_period(self,locator,period):
        eval_period=Select(self.search_element(locator))
        eval_period.select_by_visible_text(period)

    def alert_notifi_severity(self,locator,severity):
        severity_values=Select(self.search_element(locator))
        severity_values.select_by_visible_text(severity)

    def alert_notifi_category(self,locator,category):
        category_values=Select(self.search_element(locator))
        category_values.select_by_visible_text(category)

    #API Alert:
    def eval_frequency(self,locator,frequency):
        frequency_values=Select(self.search_element(locator))
        frequency_values.select_by_visible_text(frequency)

    #Server Configuration:
    def server_owner(self,locator,owner):
        owners=Select(self.search_element(locator))
        owners.select_by_visible_text(owner)


    #External Tools:
    def tools_type(self,locator,tool):
        tools=Select(self.search_element(locator))
        tools.select_by_visible_text(tool)

    def environment(self,locator,environment):
        environments=Select(self.search_element(locator))
        environments.select_by_visible_text(environment)

    def protocol(self,locator,protocol):
        protocols=Select(self.search_element(locator))
        protocols.select_by_visible_text(protocol)

    def Auth_type(self,locator,auths):
        Auth_types=Select(self.search_element(locator))
        Auth_types.select_by_visible_text(auths)










