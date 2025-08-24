from POM.Log_Management import Log_management
import allure
from time import sleep

def test_log_details(server):
    """
    Before Executing Test Cases, Change the Test data
    """
    log_detail=Log_management(server)
    log_detail.log_details('check kubernetes','🕒 Last 12h','🔽 All Levels','All Sources')

def test_All_logs(server):
    """
    Before Executing Test Cases, Change the Test data
    """
    log_detail=Log_management(server)
    log_detail.logs('Mule test server','🕒 Last 1h','🔴 Error','All Sources')