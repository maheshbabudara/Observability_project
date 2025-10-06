import os
location=os.getcwd()
import tempfile
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions, Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeDriver, WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest

@pytest.fixture(params=['chrome', 'edge', 'firefox'])
def login(request):
    browser = request.param
    username = "adminmpulse@gmail.com"
    password = "Admin@123"
    location = tempfile.mkdtemp()  # create a temp folder for downloads

    if browser == "chrome":
        option = ChromeOptions()
        option.add_experimental_option("detach", True)
        preferences = {
            "download.default_directory": location,
            "plugins.always_open_pdf_externally": True
        }
        option.add_experimental_option("prefs", preferences)
        option.add_argument("--disable-notifications")
        option.add_argument("--allow-running-insecure-content")
        option.add_argument("--disable-web-security")
        # option.add_argument("--headless")
        driver = ChromeDriver(options=option)
        driver.get("http://13.202.80.237:8080/mpulseSSO/#/")
        driver.maximize_window()

        # driver.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
        # driver.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
        # sleep(1)

        # driver.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
        # sleep(1)

    elif browser == "edge":
        option = EdgeOptions()
        from selenium.webdriver.edge.service import Service as EdgeService

        EDGE_DRIVER_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # update this path

        # option = EdgeOptions()
        service = EdgeService(executable_path=EDGE_DRIVER_PATH)
        driver = EdgeDriver(service=service, options=option)

        option.add_argument("--disable-notifications")
        option.add_argument("--allow-running-insecure-content")
        option.add_argument("--disable-web-security")
        option.add_experimental_option("detach", True)
        preferences = {
            "download.default_directory": location,
            "plugins.always_open_pdf_externally": True
        }
        option.add_experimental_option("prefs", preferences)
        driver = EdgeDriver(options=option)
        driver.get("http://13.202.80.237:8080/mpulseSSO/#/")
        driver.maximize_window()


    elif browser == "firefox":
        option = FirefoxOptions()
        # option.add_argument("--headless")
        FIREFOX_DRIVER_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # adjust if using manually

        # option = FirefoxOptions()
        # option.add_argument("--headless")  # Uncomment to run headless
        option.set_preference("dom.webnotifications.enabled", False)
        option.set_preference("security.mixed_content.block_active_content", False)
        option.set_preference("security.mixed_content.block_display_content", False)

        # Download settings
        option.set_preference("browser.download.dir", location)
        option.set_preference("browser.download.folderList", 2)  # 0: desktop, 1: default, 2: custom dir
        option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/octet-stream")
        option.set_preference("pdfjs.disabled", True)  # Disable built-in PDF viewer

        # Optional: to avoid "open with/save file" dialog
        option.set_preference("browser.download.manager.showWhenStarting", False)

        # Start Firefox driver
        service = FirefoxService(executable_path=FIREFOX_DRIVER_PATH)
        driver = FirefoxDriver(service=service, options=option)
        driver.get("http://13.202.80.237:8080/mpulseSSO/#/")
        driver.maximize_window()
        driver.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
        driver.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
        sleep(1)
        driver.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
        sleep(1)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver

    driver.quit()


#Commented to CI/CD EXECUTION SETUP:
# @pytest.fixture()
# def server():
#     username = "adminmpulse@gmail.com"
#     password = "Admin@123"
#     option=ChromeOptions()
#     option.add_argument("--disable-notifications")
#     # option.add_argument('--headless')
#     option.add_experimental_option("detach",True)
#     preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
#     option.add_experimental_option("prefs",preferences)
#     option.add_argument("--allow-running-insecure-content")
#     option.add_argument("--disable-web-security")
#     server=WebDriver(options=option)
#     server.get("http://13.202.80.237:8080/mpulseSSO/#/")
#     server.implicitly_wait(10)
#     server.maximize_window()
#     server.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
#     server.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
#     server.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
#     # server.find_element('xpath', '//img[contains(@src,"assets/M-Pulse")]/../ancestor::div[@class="ant-col ant-col-8 ng-star-inserted"]').click()
#     server.find_element('xpath',
#                         '//*[@ng-reflect-title="OBSERVABILITY"]').click()
#     sleep(1)
#     yield server
#     server.quit()


# from selenium.webdriver import Chrome, ChromeOptions
# import tempfile
# import pytest
# import os

@pytest.fixture()
def server():
    username = "adminmpulse@gmail.com"
    password = "Admin@123"

    location = os.path.abspath("downloads")
    os.makedirs(location, exist_ok=True)

    option = ChromeOptions()
    option.add_argument("--disable-notifications")
    option.add_argument("--headless=new")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--allow-running-insecure-content")
    option.add_argument("--disable-web-security")

    preferences = {
        "download.default_directory": location,
        "plugins.always_open_pdf_externally": True
    }
    option.add_experimental_option("prefs", preferences)

    # ✅ Avoid user-data-dir conflict
    option.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    server = WebDriver(options=option)
    server.get("http://13.202.80.237:8080/mpulseSSO/#/")
    server.implicitly_wait(10)
    server.maximize_window()
    server.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
    server.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
    server.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
    # server.find_element('xpath', '//img[contains(@src,"assets/M-Pulse")]/../ancestor::div[@class="ant-col ant-col-8 ng-star-inserted"]').click()
    server.find_element('xpath',
                            '//*[@ng-reflect-title="OBSERVABILITY"]').click()
    sleep(1)

    yield server
    server.quit()


@pytest.fixture()
def global_config():
    username = "adminmpulse@gmail.com"
    password = "Admin@123"
    option=ChromeOptions()
    option.add_argument("--disable-notifications")
    # option.add_argument('--headless')
    option.add_experimental_option("detach",True)
    preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    option.add_experimental_option("prefs",preferences)
    option.add_argument("--allow-running-insecure-content")
    option.add_argument("--disable-web-security")
    global_config=WebDriver(options=option)
    global_config.get("http://13.202.80.237:8080/mpulseSSO/#/")
    global_config.implicitly_wait(10)
    global_config.maximize_window()
    global_config.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
    global_config.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
    global_config.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
    global_config.find_element('xpath', '//img[contains(@src,"assets/M-Pulse")]/../ancestor::div[@class="ant-col ant-col-8 ng-star-inserted"]').click()
    sleep(1)
    yield global_config
    global_config.quit()

@pytest.fixture()
def ms_access():
    username="observabilityadmin@gmail.com"
    password="Admin@123"
    option = ChromeOptions()
    option.add_argument("--disable-notifications")
    option.add_experimental_option("detach",True)
    preferences={"download.default_directory":location, "plugins.always_open_pdf_externally":True}
    option.add_experimental_option('prefs',preferences)
    option.add_argument("--allow-running-insecure-content")
    option.add_argument("--disable-web-security")
    ms_access=WebDriver(options=option)
    ms_access.implicitly_wait(10)
    ms_access.get("http://13.202.80.237:8080/mpulseSSO/#/")
    ms_access.maximize_window()
    ms_access.find_element("xpath", '//input[@placeholder="Enter your email"]').send_keys(username)
    ms_access.find_element("xpath", '//input[@placeholder="Enter your password"]').send_keys(password)
    ms_access.find_element("xpath", "//button[contains(text(),'Sign In')]").click()
    ms_access.find_element('xpath', '//img[contains(@src,"assets/M-Pulse")]/../ancestor::div[@class="ant-col ant-col-8 ng-star-inserted"]').click()
    sleep(1)

    yield ms_access
    ms_access.quit()














