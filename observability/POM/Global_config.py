from unicodedata import category

from Library.library import Base
from time import sleep
from Utilities.Global_config import metric, API, application


class config(Base):
    def create_metrics(self, alert_type, alert_details, metrics,
                       severity, category, threshold,evalution_period,
                       app_name,app_id,phone_no,trigger_count,receiver_emails,
                       server,server_ip=None,server_name=None):
        self.zoomout()
        self.click(metric.global_config)
        sleep(1)
        self.alert_select(metric.alert_type,alert_type)
        sleep(1)
        self.send_data(metric.alert_details,alert_details)
        sleep(1)
        self.metrics_name(metric.alert_property_name,metrics)
        sleep(1)
        self.alert_severity(metric.severity,severity)
        sleep(1)
        self.alert_category(metric.category,category)
        sleep(1)
        self.clear(metric.threshold)
        self.send_data(metric.threshold,threshold)
        sleep(1)
        self.eval_period(metric.evalution_period,evalution_period)
        sleep(1)
        self.send_data(metric.app_name, app_name)
        sleep(1)
        self.send_data(metric.app_id,app_id)
        sleep(1)
        self.send_data(metric.phn,phone_no)
        sleep(1)
        self.clear(metric.trigger_count)
        self.send_data(metric.trigger_count, trigger_count)
        sleep(1)
        self.send_data(metric.receiver_emails, receiver_emails)
        sleep(1)
        self.server_select(metric.server,server)
        # self.send_data(metric.serverip,server_ip)  #AUTO FILL Field
        # self.send_data(metric.server_name, server_name)#AUTO FILL Field
        sleep(3)
        self.scroll(metric.create_btn)
        sleep(1)
        self.global_config_click(metric.create_btn)

    def api(self, alert_type, alert_details, api,
                       severity, category, threshold,evalution_period,api_appname,api_path,status_code,
                       app_name,app_id,phone_no,trigger_count,receiver_emails,
                       server,server_ip=None,server_name=None):
        self.zoomout()
        self.click(API.global_config)
        sleep(1)
        self.alert_select(API.alert_type,alert_type)
        sleep(1)
        self.send_data(API.alert_details,alert_details)
        sleep(1)
        self.API_name(API.alert_property_name,api)
        sleep(1)
        self.alert_severity(API.severity,severity)
        sleep(1)
        self.alert_category(API.category,category)
        sleep(1)
        self.clear(API.threshold)
        self.send_data(API.threshold,threshold)
        sleep(1)
        self.eval_period(API.evalution_period,evalution_period)
        sleep(1)
        self.send_data(API.api_appname,api_appname)
        sleep(1)
        self.send_data(API.api_path, api_path)
        sleep(1)
        self.send_data(API.status_code, status_code)
        sleep(1)
        self.send_data(API.app_name, app_name)
        sleep(1)
        self.send_data(API.app_id,app_id)
        sleep(1)
        self.send_data(API.phn,phone_no)
        sleep(1)
        self.clear(API.trigger_count)
        self.send_data(API.trigger_count, trigger_count)
        sleep(1)
        self.send_data(API.receiver_emails, receiver_emails)
        sleep(1)
        self.server_select(API.server,server)
        # self.send_data(metric.serverip,server_ip)  #AUTO FILL Field
        # self.send_data(metric.server_name, server_name)#AUTO FILL Field
        sleep(3)
        self.scroll(API.create_btn)
        sleep(1)
        self.global_config_click(API.create_btn)

    def application(self, alert_type, alert_details, app,
                       severity, category, threshold,evalution_period,application_name,latency_bucket,
                       app_name,app_id,phone_no,trigger_count,receiver_emails,
                       server,server_ip=None,server_name=None):
        self.zoomout()
        self.click(application.global_config)
        sleep(1)
        self.alert_select(application.alert_type,alert_type)
        sleep(1)
        self.send_data(application.alert_details,alert_details)
        sleep(1)
        self.Application(application.alert_property_name,app)
        sleep(1)
        self.alert_severity(application.severity,severity)
        sleep(1)
        self.alert_category(application.category,category)
        sleep(1)
        self.clear(application.threshold)
        self.send_data(application.threshold,threshold)
        sleep(1)
        self.eval_period(application.evalution_period,evalution_period)
        sleep(1)
        self.send_data(application.application_name,application_name)
        sleep(1)
        self.send_data(application.latency_bucket,latency_bucket)
        sleep(1)
        self.send_data(application.app_name, app_name)
        sleep(1)
        self.send_data(application.app_id,app_id)
        sleep(1)
        self.send_data(application.phn,phone_no)
        sleep(1)
        self.clear(application.trigger_count)
        self.send_data(application.trigger_count, trigger_count)
        sleep(1)
        self.send_data(application.receiver_emails, receiver_emails)
        sleep(1)
        self.server_select(application.server,server)
        # self.send_data(metric.serverip,server_ip)  #AUTO FILL Field
        # self.send_data(metric.server_name, server_name)#AUTO FILL Field
        sleep(3)
        self.scroll(application.create_btn)
        sleep(1)
        self.global_config_click(application.create_btn)



