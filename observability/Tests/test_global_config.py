from POM.Global_config import config
from time import sleep
import allure

def test_global_Metrics(global_config):
    """

    :param global_config:
    :return:
    """
    metric=config(global_config)
    metric.create_metrics('METRICS','Automation Purpose','CriticalMemoryUsage',
                          'Critical','Performance'
                          ,'20','10 minutes','Hafen','123',
                          '86392516301','10',
                          'mahehs.babu@maiora.co','test Kubenetes',None,None)

def test_global_API(global_config):
    metric=config(global_config)
    metric.api('API','Automation Purpose','request_volume_spike',
                          'Critical','Security'
                          ,'20','5 minutes','Testing','test\check\kubernetes','200','Hafen-1','123',
                          '86392516301','10',
                          'mahehs.babu@maiora.co','test Kubenetes',None,None)

def test_global_Application(global_config):
    metric=config(global_config)
    metric.application('APPLICATION','Automation Purpose','AppCPUUtilization',
                          'High','Application'
                          ,'10','30 minutes','Testing','30-40','Hafen-1','123',
                          '86392516301','20',
                          'mahehs.babu@maiora.co','test Kubenetes',None,None)