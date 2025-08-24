from POM.Dashboard import Dashboard
from time import sleep
import allure

def test_dashboard(server):
    dashboard=Dashboard(server)
    dashboard.dash_details()