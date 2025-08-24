from Library.library import Base
from time import sleep
from Utilities.alerts_notifi_locator import server_alerts,API_alerts,application_alerts,alert_rules

class alert_noti(Base):
    #Server alert Feature:
    def server_app_alert(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,alert_appname, latency_bucket,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(server_alerts.alert_notifi_locator)
        self.click(server_alerts.alert_btn)
        self.alert_notifi_type(server_alerts.type_loc,type_value)
        self.alert_notifi_server(server_alerts.server_loc,server_value)
        self.alert_notifi_app(server_alerts.application_loc,app_value)
        self.send_data(server_alerts.alertname_loc,alertname)
        self.send_data(server_alerts.triggercount_loc,triggercount)
        self.alert_notifi_propertyname(server_alerts.alertprop_loc,propertyname)
        self.alert_evalution_period(server_alerts.evalution_period,period)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc,threshold)
        self.send_data(server_alerts.alert_appname_loc,alert_appname)
        self.send_data(server_alerts.latency_bucket_loc, latency_bucket)

        self.alert_notifi_severity(server_alerts.severity_loc, severity)
        self.alert_notifi_category(server_alerts.category_loc,alert_category)
        self.send_data(server_alerts.emailreceiptents_loc, email)
        self.send_data(server_alerts.phonenumbers_loc, phone_no)
        self.scroll(server_alerts.alert_accept)
        self.click(server_alerts.alert_accept)

    def server_metrics_alert(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(server_alerts.alert_notifi_locator)
        self.click(server_alerts.alert_btn)
        self.alert_notifi_type(server_alerts.type_loc,type_value)
        self.alert_notifi_server(server_alerts.server_loc,server_value)
        self.alert_notifi_app(server_alerts.application_loc,app_value)
        self.send_data(server_alerts.alertname_loc,alertname)
        self.send_data(server_alerts.triggercount_loc,triggercount)

        self.alert_notifi_propertyname(server_alerts.alertprop_loc,propertyname)
        self.alert_evalution_period(server_alerts.evalution_period,period)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc,threshold)


        self.alert_notifi_severity(server_alerts.severity_loc, severity)
        self.alert_notifi_category(server_alerts.category_loc,alert_category)
        self.send_data(server_alerts.emailreceiptents_loc, email)
        self.send_data(server_alerts.phonenumbers_loc, phone_no)
        self.scroll(server_alerts.alert_accept)
        self.click(server_alerts.alert_accept)

    def server_API_alert(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,alert_appname,api_path,status_code,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(server_alerts.alert_notifi_locator)
        self.click(server_alerts.alert_btn)
        self.alert_notifi_type(server_alerts.type_loc,type_value)
        self.alert_notifi_server(server_alerts.server_loc,server_value)
        self.alert_notifi_app(server_alerts.application_loc,app_value)
        self.send_data(server_alerts.alertname_loc,alertname)
        self.send_data(server_alerts.triggercount_loc,triggercount)

        self.alert_notifi_propertyname(server_alerts.alertprop_loc,propertyname)
        self.alert_evalution_period(server_alerts.evalution_period,period)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc,threshold)
        self.send_data(server_alerts.alert_appname_loc,alert_appname)
        self.send_data(server_alerts.status_code,status_code)
        self.send_data(server_alerts.api_path_loc, api_path)

        self.alert_notifi_severity(server_alerts.severity_loc, severity)
        self.alert_notifi_category(server_alerts.category_loc,alert_category)
        self.send_data(server_alerts.emailreceiptents_loc, email)
        self.send_data(server_alerts.phonenumbers_loc, phone_no)
        self.scroll(server_alerts.alert_accept)
        self.click(server_alerts.alert_accept)

    # API alert Feature:
    def API_alert(self, api_url,
                  api_key1, api_value1, api_unit1,
                  api_key2, api_value2, api_unit2,
                  api_key3, api_value3, api_unit3,
                  eval_frequency, email, phone_no,message):
        """
        Define the api key,value, unit as per the API requirement
        """
        self.zoomout()
        self.click(API_alerts.alert_notifi_locator)
        self.click(API_alerts.api_alert_loc)
        self.click(API_alerts.alert_btn)
        self.send_data(API_alerts.api_url, api_url)

        self.send_data(API_alerts.api_alert_key,api_key1)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value1)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit,api_unit1)
        sleep(1)
        self.click(API_alerts.add_property)  #Add New Property
        sleep(1)
        #Another property adding:
        self.send_data(API_alerts.api_alert_key, api_key2)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value2)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit, api_unit2)
        sleep(1)

        self.click(API_alerts.add_property)
        sleep(1)
        self.send_data(API_alerts.api_alert_key, api_key3)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value3)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit, api_unit3)
        sleep(1)
        self.click(API_alerts.delete_property) #Remove property
        sleep(1)

        self.scroll(API_alerts.optional_settings)
        sleep(1)
        self.click(API_alerts.optional_settings)
        sleep(1)
        self.eval_frequency(API_alerts.eval_frequency,eval_frequency)
        sleep(1)
        self.scroll(API_alerts.enable_immediatly)
        sleep(1)
        self.click(API_alerts.enable_immediatly)  #Disbale Immediately
        sleep(1)
        self.click(API_alerts.enable_immediatly)  #Enabale Immediately

        self.send_data(API_alerts.emailreceiptents_loc, email)
        sleep(1)
        self.send_data(API_alerts.phonenumbers_loc, phone_no)
        sleep(1)
        self.send_data(API_alerts.message_loc,message)
        sleep(1)
        self.click(API_alerts.save_config)
        sleep(5)

    #Application alert Feature:
    def application_app_alert(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,alert_appname, latency_bucket,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(application_alerts.alert_notifi_locator)
        self.click(application_alerts.application_feature) # Clicking on Application Feature
        # self.driver.refresh()
        sleep(5)
        self.click(application_alerts.alert_btn)
        self.alert_notifi_type(application_alerts.type_loc,type_value)
        self.alert_notifi_server(application_alerts.server_loc,server_value)
        self.alert_notifi_app(application_alerts.application_loc,app_value)
        self.send_data(application_alerts.alertname_loc,alertname)
        self.send_data(application_alerts.triggercount_loc,triggercount)
        self.alert_notifi_propertyname(application_alerts.alertprop_loc,propertyname)
        self.alert_evalution_period(application_alerts.evalution_period,period)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc,threshold)
        self.send_data(application_alerts.alert_appname_loc,alert_appname)
        self.send_data(application_alerts.latency_bucket_loc, latency_bucket)

        self.alert_notifi_severity(application_alerts.severity_loc, severity)
        self.alert_notifi_category(application_alerts.category_loc,alert_category)
        self.send_data(application_alerts.emailreceiptents_loc, email)
        self.send_data(application_alerts.phonenumbers_loc, phone_no)
        self.scroll(application_alerts.alert_accept)
        self.click(application_alerts.alert_accept)

    def application_metrics_alert(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(application_alerts.alert_notifi_locator)
        self.click(application_alerts.application_feature) # Clicking on Application Feature
        self.click(application_alerts.alert_btn)
        self.alert_notifi_type(application_alerts.type_loc,type_value)
        self.alert_notifi_server(application_alerts.server_loc,server_value)
        self.alert_notifi_app(application_alerts.application_loc,app_value)
        self.send_data(application_alerts.alertname_loc,alertname)
        self.send_data(application_alerts.triggercount_loc,triggercount)

        self.alert_notifi_propertyname(application_alerts.alertprop_loc,propertyname)
        self.alert_evalution_period(application_alerts.evalution_period,period)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc,threshold)


        self.alert_notifi_severity(application_alerts.severity_loc, severity)
        self.alert_notifi_category(application_alerts.category_loc,alert_category)
        self.send_data(application_alerts.emailreceiptents_loc, email)
        self.send_data(application_alerts.phonenumbers_loc, phone_no)
        self.scroll(application_alerts.alert_accept)
        self.click(application_alerts.alert_accept)

    def application_API_alert(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,alert_appname,api_path,status_code,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(application_alerts.alert_notifi_locator)
        self.click(application_alerts.application_feature) # Clicking on Application Feature
        self.click(application_alerts.alert_btn)
        self.alert_notifi_type(application_alerts.type_loc,type_value)
        self.alert_notifi_server(application_alerts.server_loc,server_value)
        self.alert_notifi_app(application_alerts.application_loc,app_value)
        self.send_data(application_alerts.alertname_loc,alertname)
        self.send_data(application_alerts.triggercount_loc,triggercount)

        self.alert_notifi_propertyname(application_alerts.alertprop_loc,propertyname)
        self.alert_evalution_period(application_alerts.evalution_period,period)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc,threshold)
        self.send_data(application_alerts.alert_appname_loc,alert_appname)
        self.send_data(application_alerts.status_code,status_code)
        self.send_data(application_alerts.api_path_loc, api_path)

        self.alert_notifi_severity(application_alerts.severity_loc, severity)
        self.alert_notifi_category(application_alerts.category_loc,alert_category)
        self.send_data(application_alerts.emailreceiptents_loc, email)
        self.send_data(application_alerts.phonenumbers_loc, phone_no)
        self.scroll(application_alerts.alert_accept)
        self.click(application_alerts.alert_accept)

    #Alert Rule:
    def Alert_Rules_app(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,alert_appname, latency_bucket,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(alert_rules.alert_notifi_locator)
        self.click(alert_rules.alert_rules_feature)
        # self.driver.refresh()
        sleep(5)
        self.click(alert_rules.alert_btn)
        self.alert_notifi_type(alert_rules.type_loc,type_value)
        self.alert_notifi_server(alert_rules.server_loc,server_value)
        self.alert_notifi_app(alert_rules.application_loc,app_value)
        self.send_data(alert_rules.alertname_loc,alertname)
        self.send_data(alert_rules.triggercount_loc,triggercount)
        self.alert_notifi_propertyname(alert_rules.alertprop_loc,propertyname)
        self.alert_evalution_period(alert_rules.evalution_period,period)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc,threshold)
        self.send_data(alert_rules.alert_appname_loc,alert_appname)
        self.send_data(alert_rules.latency_bucket_loc, latency_bucket)

        self.alert_notifi_severity(alert_rules.severity_loc, severity)
        self.alert_notifi_category(alert_rules.category_loc,alert_category)
        self.send_data(alert_rules.emailreceiptents_loc, email)
        self.send_data(alert_rules.phonenumbers_loc, phone_no)
        self.scroll(alert_rules.alert_accept)
        self.click(alert_rules.alert_accept)

    def Alert_Rules_metrics(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(alert_rules.alert_notifi_locator)
        self.click(alert_rules.alert_rules_feature)
        self.click(alert_rules.alert_btn)
        sleep(5)
        self.alert_notifi_type(alert_rules.type_loc,type_value)
        self.alert_notifi_server(alert_rules.server_loc,server_value)
        self.alert_notifi_app(alert_rules.application_loc,app_value)
        self.send_data(alert_rules.alertname_loc,alertname)
        self.send_data(alert_rules.triggercount_loc,triggercount)

        self.alert_notifi_propertyname(alert_rules.alertprop_loc,propertyname)
        self.alert_evalution_period(alert_rules.evalution_period,period)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc,threshold)


        self.alert_notifi_severity(alert_rules.severity_loc, severity)
        self.alert_notifi_category(alert_rules.category_loc,alert_category)
        self.send_data(alert_rules.emailreceiptents_loc, email)
        self.send_data(alert_rules.phonenumbers_loc, phone_no)
        self.scroll(alert_rules.alert_accept)
        self.click(alert_rules.alert_accept)

    def Alert_Rules_API(self, type_value,server_value,app_value,alertname,triggercount,propertyname,period,
               threshold,alert_appname,api_path,status_code,severity,alert_category,email,phone_no):
        self.zoomout()
        self.click(alert_rules.alert_notifi_locator)
        self.click(alert_rules.alert_rules_feature)
        self.click(alert_rules.alert_btn)

        self.alert_notifi_type(alert_rules.type_loc,type_value)
        # sleep(5)
        self.alert_notifi_server(alert_rules.server_loc,server_value)
        self.alert_notifi_app(alert_rules.application_loc,app_value)
        self.send_data(alert_rules.alertname_loc,alertname)
        self.send_data(alert_rules.triggercount_loc,triggercount)

        self.alert_notifi_propertyname(alert_rules.alertprop_loc,propertyname)
        self.alert_evalution_period(alert_rules.evalution_period,period)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc,threshold)
        self.send_data(alert_rules.alert_appname_loc,alert_appname)
        self.send_data(alert_rules.status_code,status_code)
        self.send_data(alert_rules.api_path_loc, api_path)

        self.alert_notifi_severity(alert_rules.severity_loc, severity)
        self.alert_notifi_category(alert_rules.category_loc,alert_category)
        self.send_data(alert_rules.emailreceiptents_loc, email)
        self.send_data(alert_rules.phonenumbers_loc, phone_no)
        self.scroll(alert_rules.alert_accept)
        self.click(alert_rules.alert_accept)

    #Multiple Server Alerts:
    def server_multi_app_alert(self, type_value1,server_value1,app_value1,alert_name1,
                               trigger_count1,property_name1,period1,threshold1,alert_appname1,
                               latency_bucket1,severity1,alert_category1,email1,phone_no1,
                               type_value2, server_value2, app_value2, alert_name2,
                               trigger_count2, property_name2, period2, threshold2, alert_appname2,
                               latency_bucket2, severity2, alert_category2, email2, phone_no2
                               ):
        self.zoomout()
        self.click(server_alerts.alert_notifi_locator)
        self.click(server_alerts.alert_btn)
        self.alert_notifi_type(server_alerts.type_loc,type_value1)
        self.alert_notifi_server(server_alerts.server_loc,server_value1)
        self.alert_notifi_app(server_alerts.application_loc,app_value1)
        self.send_data(server_alerts.alertname_loc,alert_name1)
        self.send_data(server_alerts.triggercount_loc,trigger_count1)
        self.alert_notifi_propertyname(server_alerts.alertprop_loc,property_name1)
        self.alert_evalution_period(server_alerts.evalution_period,period1)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc,threshold1)
        self.send_data(server_alerts.alert_appname_loc,alert_appname1)
        self.send_data(server_alerts.latency_bucket_loc, latency_bucket1)

        self.alert_notifi_severity(server_alerts.severity_loc, severity1)
        self.alert_notifi_category(server_alerts.category_loc,alert_category1)
        self.send_data(server_alerts.emailreceiptents_loc, email1)
        self.send_data(server_alerts.phonenumbers_loc, phone_no1)


        #Adding Second Alert:
        self.scroll(server_alerts.add_alert)
        sleep(1)
        self.click(server_alerts.add_alert)
        sleep(1)
        self.alert_notifi_type(server_alerts.type_loc,type_value2)
        self.alert_notifi_server(server_alerts.server_loc,server_value2)
        self.alert_notifi_app(server_alerts.application_loc,app_value2)
        self.send_data(server_alerts.alertname_loc,alert_name2)
        self.send_data(server_alerts.triggercount_loc,trigger_count2)
        self.alert_notifi_propertyname(server_alerts.alertprop_loc,property_name2)
        self.alert_evalution_period(server_alerts.evalution_period,period2)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc,threshold2)

        #If user try to create with Metrics alert the below code not required
        # self.send_data(server_alerts.alert_appname_loc,alert_appname2)
        # self.send_data(server_alerts.latency_bucket_loc, latency_bucket2)

        self.alert_notifi_severity(server_alerts.severity_loc, severity2)
        self.alert_notifi_category(server_alerts.category_loc,alert_category2)
        self.send_data(server_alerts.emailreceiptents_loc, email2)
        self.send_data(server_alerts.phonenumbers_loc, phone_no2)

        #submit Alerts:
        self.scroll(server_alerts.alert_accept)
        self.click(server_alerts.alert_accept)


    def server_multi_metrics_alert(self, type_value1,server_value1,app_value1,
                                   alert_name1,trigger_count1,property_name1,period1,threshold1,
                                   severity1,alert_category1,email1,phone_no1,
                                   type_value2, server_value2, app_value2, alert_name2, trigger_count2,
                                   property_name2,period2,threshold2, alert_appname2, api_path, status_code,
                                   severity2, alert_category2,email2,phone_no2
                                   ):
        self.zoomout()
        self.click(server_alerts.alert_notifi_locator)
        self.click(server_alerts.alert_btn)
        self.alert_notifi_type(server_alerts.type_loc,type_value1)
        self.alert_notifi_server(server_alerts.server_loc,server_value1)
        self.alert_notifi_app(server_alerts.application_loc,app_value1)
        self.send_data(server_alerts.alertname_loc,alert_name1)
        self.send_data(server_alerts.triggercount_loc,trigger_count1)

        self.alert_notifi_propertyname(server_alerts.alertprop_loc,property_name1)
        self.alert_evalution_period(server_alerts.evalution_period,period1)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc,threshold1)


        self.alert_notifi_severity(server_alerts.severity_loc, severity1)
        self.alert_notifi_category(server_alerts.category_loc,alert_category1)
        self.send_data(server_alerts.emailreceiptents_loc, email1)
        self.send_data(server_alerts.phonenumbers_loc, phone_no1)

        #Add Alert:
        self.scroll(server_alerts.add_alert)
        sleep(1)
        self.click(server_alerts.add_alert)
        sleep(1)
        self.alert_notifi_type(server_alerts.type_loc, type_value2)
        self.alert_notifi_server(server_alerts.server_loc, server_value2)
        self.alert_notifi_app(server_alerts.application_loc, app_value2)
        self.send_data(server_alerts.alertname_loc, alert_name2)
        self.send_data(server_alerts.triggercount_loc, trigger_count2)

        self.alert_notifi_propertyname(server_alerts.alertprop_loc, property_name2)
        self.alert_evalution_period(server_alerts.evalution_period, period2)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc, threshold2)
        self.send_data(server_alerts.alert_appname_loc, alert_appname2)
        self.send_data(server_alerts.status_code, status_code)
        self.send_data(server_alerts.api_path_loc, api_path)

        self.alert_notifi_severity(server_alerts.severity_loc, severity2)
        self.alert_notifi_category(server_alerts.category_loc, alert_category2)
        self.send_data(server_alerts.emailreceiptents_loc, email2)
        self.send_data(server_alerts.phonenumbers_loc, phone_no2)


        #Submitting Multiple Alerts:
        self.scroll(server_alerts.alert_accept)
        self.click(server_alerts.alert_accept)


    def server_multi_API_alert(self, type_value1,server_value1,app_value1,alert_name1,trigger_count1,property_name1,
                               period1,threshold1,alert_appname1,api_path,status_code,severity1,
                               alert_category1,email1,phone_no1,
                               type_value2, server_value2, app_value2, alert_name2,
                               trigger_count2, property_name2, period2, threshold2, alert_appname2,
                               latency_bucket2, severity2, alert_category2, email2, phone_no2
                               ):
        self.zoomout()
        self.click(server_alerts.alert_notifi_locator)
        self.click(server_alerts.alert_btn)
        self.alert_notifi_type(server_alerts.type_loc,type_value1)
        self.alert_notifi_server(server_alerts.server_loc,server_value1)
        self.alert_notifi_app(server_alerts.application_loc,app_value1)
        self.send_data(server_alerts.alertname_loc,alert_name1)
        self.send_data(server_alerts.triggercount_loc,trigger_count1)

        self.alert_notifi_propertyname(server_alerts.alertprop_loc,property_name1)
        self.alert_evalution_period(server_alerts.evalution_period,period1)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc,threshold1)
        self.send_data(server_alerts.alert_appname_loc,alert_appname1)
        self.send_data(server_alerts.status_code,status_code)
        self.send_data(server_alerts.api_path_loc, api_path)

        self.alert_notifi_severity(server_alerts.severity_loc, severity1)
        self.alert_notifi_category(server_alerts.category_loc,alert_category1)
        self.send_data(server_alerts.emailreceiptents_loc, email1)
        self.send_data(server_alerts.phonenumbers_loc, phone_no1)
        sleep(1)


        #Add Alert:
        self.scroll(server_alerts.add_alert)
        sleep(1)
        self.click(server_alerts.add_alert)
        sleep(1)
        self.alert_notifi_type(server_alerts.type_loc, type_value2)
        sleep(1)
        self.alert_notifi_server(server_alerts.server_loc, server_value2)
        sleep(1)
        self.alert_notifi_app(server_alerts.application_loc, app_value2)
        self.send_data(server_alerts.alertname_loc, alert_name2)
        self.send_data(server_alerts.triggercount_loc, trigger_count2)
        self.alert_notifi_propertyname(server_alerts.alertprop_loc, property_name2)
        self.alert_evalution_period(server_alerts.evalution_period, period2)
        self.clear(server_alerts.threshold_loc)
        self.send_data(server_alerts.threshold_loc, threshold2)
        self.send_data(server_alerts.alert_appname_loc, alert_appname2)
        self.send_data(server_alerts.latency_bucket_loc, latency_bucket2)

        self.alert_notifi_severity(server_alerts.severity_loc, severity2)
        self.alert_notifi_category(server_alerts.category_loc, alert_category2)
        self.send_data(server_alerts.emailreceiptents_loc, email2)
        self.send_data(server_alerts.phonenumbers_loc, phone_no2)

        #Submitting Multiple Alerts:
        self.scroll(server_alerts.alert_accept)
        self.click(server_alerts.alert_accept)
        sleep(1)


    # API Multiple alerts:
    def API_Multi_alert(self, api_url1,
                      api_key1, api_value1, api_unit1,
                      api_key2, api_value2, api_unit2,
                      api_key3, api_value3, api_unit3,
                      eval_frequency1, email1, phone_no1, message1,
                      api_url2,
                      api_key4, api_value4, api_unit4,
                      api_key5, api_value5, api_unit5,
                      eval_frequency2, email2, phone_no2, message2
                        ):
        """
        Define the api key,value, unit as per the API requirement
        """
        self.zoomout()
        self.click(API_alerts.alert_notifi_locator)
        self.click(API_alerts.api_alert_loc)

        # Adding Alert1:
        self.click(API_alerts.alert_btn)
        self.send_data(API_alerts.api_url, api_url1)
        self.send_data(API_alerts.api_alert_key, api_key1)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value1)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit, api_unit1)
        sleep(1)
        self.click(API_alerts.add_property)  # Add New Property
        sleep(1)

        # Another property adding:
        self.send_data(API_alerts.api_alert_key, api_key2)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value2)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit, api_unit2)
        sleep(1)

        self.click(API_alerts.add_property)
        sleep(1)
        self.send_data(API_alerts.api_alert_key, api_key3)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value3)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit, api_unit3)
        sleep(1)
        self.click(API_alerts.delete_property)  # Remove property
        sleep(1)

        self.scroll(API_alerts.optional_settings)
        sleep(1)
        self.click(API_alerts.optional_settings)
        sleep(1)
        self.eval_frequency(API_alerts.eval_frequency, eval_frequency1)
        sleep(1)
        self.scroll(API_alerts.enable_immediatly)
        sleep(1)
        self.click(API_alerts.enable_immediatly)  # Disbale Immediately
        sleep(1)
        self.click(API_alerts.enable_immediatly)  # Enabale Immediately

        self.send_data(API_alerts.emailreceiptents_loc, email1)
        sleep(1)
        self.send_data(API_alerts.phonenumbers_loc, phone_no1)
        sleep(1)
        self.send_data(API_alerts.message_loc, message1)
        sleep(1)

        #Adding another alert2:
        self.scroll(API_alerts.add_alert)
        sleep(1)
        self.click(API_alerts.add_alert)
        sleep(1)
        self.clear(API_alerts.api_url)
        sleep(1)
        self.send_data(API_alerts.api_url, api_url2)
        sleep(1)
        self.send_data(API_alerts.api_alert_key, api_key4)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value4)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit, api_unit4)
        sleep(1)
        self.click(API_alerts.add_property)  # Add New Property
        sleep(1)

        # Another property adding:
        self.send_data(API_alerts.api_alert_key, api_key5)
        sleep(1)
        self.send_data(API_alerts.api_alert_value, api_value5)
        sleep(1)
        self.send_data(API_alerts.api_alert_unit, api_unit5)
        sleep(1)

        option=('xpath','//span[@class="settings-title"]')
        self.scroll(option)
        sleep(1)
        # self.click(API_alerts.optional_settings)
        # sleep(1)
        self.eval_frequency(API_alerts.eval_frequency, eval_frequency2)
        sleep(1)
        self.scroll(API_alerts.enable_immediatly)
        sleep(1)
        self.click(API_alerts.enable_immediatly)  # Disbale Immediately
        sleep(1)
        self.click(API_alerts.enable_immediatly)  # Enabale Immediately

        self.send_data(API_alerts.emailreceiptents_loc, email2)
        sleep(1)
        self.send_data(API_alerts.phonenumbers_loc, phone_no2)
        sleep(1)
        self.send_data(API_alerts.message_loc, message2)
        sleep(1)

        #Submiting Alerts:
        self.scroll(API_alerts.save_config)
        sleep(1)
        self.click(API_alerts.save_config)
        sleep(1)


    #Multiple APPLICATION FEATURE Alerts:
    def application_multi_app_alert(self, type_value1,server_value1,app_value1,alert_name1,
                               trigger_count1,property_name1,period1,threshold1,alert_appname1,
                               latency_bucket1,severity1,alert_category1,email1,phone_no1,
                               type_value2, server_value2, app_value2, alert_name2,
                               trigger_count2, property_name2, period2, threshold2, alert_appname2,
                               latency_bucket2, severity2, alert_category2, email2, phone_no2
                               ):
        self.zoomout()
        self.click(application_alerts.alert_notifi_locator)
        self.click(application_alerts.application_feature)  # Clicking on Application Feature
        self.click(application_alerts.alert_btn)
        self.alert_notifi_type(application_alerts.type_loc,type_value1)
        self.alert_notifi_server(application_alerts.server_loc,server_value1)
        self.alert_notifi_app(application_alerts.application_loc,app_value1)
        self.send_data(application_alerts.alertname_loc,alert_name1)
        self.send_data(application_alerts.triggercount_loc,trigger_count1)
        self.alert_notifi_propertyname(application_alerts.alertprop_loc,property_name1)
        self.alert_evalution_period(application_alerts.evalution_period,period1)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc,threshold1)
        self.send_data(application_alerts.alert_appname_loc,alert_appname1)
        self.send_data(application_alerts.latency_bucket_loc, latency_bucket1)

        self.alert_notifi_severity(application_alerts.severity_loc, severity1)
        self.alert_notifi_category(application_alerts.category_loc,alert_category1)
        self.send_data(application_alerts.emailreceiptents_loc, email1)
        self.send_data(application_alerts.phonenumbers_loc, phone_no1)


        #Adding Second Alert:
        self.scroll(application_alerts.add_alert)
        sleep(1)
        self.click(application_alerts.add_alert)
        sleep(1)
        self.alert_notifi_type(application_alerts.type_loc,type_value2)
        self.alert_notifi_server(application_alerts.server_loc,server_value2)
        self.alert_notifi_app(application_alerts.application_loc,app_value2)
        self.send_data(application_alerts.alertname_loc,alert_name2)
        self.send_data(application_alerts.triggercount_loc,trigger_count2)
        self.alert_notifi_propertyname(application_alerts.alertprop_loc,property_name2)
        self.alert_evalution_period(application_alerts.evalution_period,period2)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc,threshold2)

        #If user try to create with Metrics alert then below code not required
        # self.send_data(application_alerts.alert_appname_loc,alert_appname2)
        # self.send_data(application_alerts.latency_bucket_loc, latency_bucket2)

        self.alert_notifi_severity(application_alerts.severity_loc, severity2)
        self.alert_notifi_category(application_alerts.category_loc,alert_category2)
        self.send_data(application_alerts.emailreceiptents_loc, email2)
        self.send_data(application_alerts.phonenumbers_loc, phone_no2)

        #submit Alerts:
        self.scroll(application_alerts.alert_accept)
        self.click(application_alerts.alert_accept)


    def application_multi_metrics_alert(self, type_value1,server_value1,app_value1,
                                   alert_name1,trigger_count1,property_name1,period1,threshold1,
                                   severity1,alert_category1,email1,phone_no1,
                                   type_value2, server_value2, app_value2, alert_name2, trigger_count2,
                                   property_name2,period2,threshold2, alert_appname2, api_path, status_code,
                                   severity2, alert_category2,email2,phone_no2
                                   ):
        self.zoomout()
        self.click(application_alerts.alert_notifi_locator)
        self.click(application_alerts.application_feature)  # Clicking on Application Feature
        self.click(application_alerts.alert_btn)
        self.alert_notifi_type(application_alerts.type_loc,type_value1)
        self.alert_notifi_server(application_alerts.server_loc,server_value1)
        self.alert_notifi_app(application_alerts.application_loc,app_value1)
        self.send_data(application_alerts.alertname_loc,alert_name1)
        self.send_data(application_alerts.triggercount_loc,trigger_count1)

        self.alert_notifi_propertyname(application_alerts.alertprop_loc,property_name1)
        self.alert_evalution_period(application_alerts.evalution_period,period1)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc,threshold1)


        self.alert_notifi_severity(application_alerts.severity_loc, severity1)
        self.alert_notifi_category(application_alerts.category_loc,alert_category1)
        self.send_data(application_alerts.emailreceiptents_loc, email1)
        self.send_data(application_alerts.phonenumbers_loc, phone_no1)

        #Add Alert:
        self.scroll(application_alerts.add_alert)
        sleep(1)
        self.click(application_alerts.add_alert)
        sleep(1)
        self.alert_notifi_type(application_alerts.type_loc, type_value2)
        self.alert_notifi_server(application_alerts.server_loc, server_value2)
        self.alert_notifi_app(application_alerts.application_loc, app_value2)
        self.send_data(application_alerts.alertname_loc, alert_name2)
        self.send_data(application_alerts.triggercount_loc, trigger_count2)

        self.alert_notifi_propertyname(application_alerts.alertprop_loc, property_name2)
        self.alert_evalution_period(application_alerts.evalution_period, period2)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc, threshold2)
        self.send_data(application_alerts.alert_appname_loc, alert_appname2)
        self.send_data(application_alerts.status_code, status_code)
        self.send_data(application_alerts.api_path_loc, api_path)

        self.alert_notifi_severity(application_alerts.severity_loc, severity2)
        self.alert_notifi_category(application_alerts.category_loc, alert_category2)
        self.send_data(application_alerts.emailreceiptents_loc, email2)
        self.send_data(application_alerts.phonenumbers_loc, phone_no2)


        #Submitting Multiple Alerts:
        self.scroll(application_alerts.alert_accept)
        self.click(application_alerts.alert_accept)


    def application_multi_API_alert(self, type_value1,server_value1,app_value1,alert_name1,trigger_count1,property_name1,
                               period1,threshold1,alert_appname1,api_path,status_code,severity1,
                               alert_category1,email1,phone_no1,
                               type_value2, server_value2, app_value2, alert_name2,
                               trigger_count2, property_name2, period2, threshold2, alert_appname2,
                               latency_bucket2, severity2, alert_category2, email2, phone_no2
                               ):
        self.zoomout()
        self.click(application_alerts.alert_notifi_locator)
        self.click(application_alerts.application_feature) #Clicking on Application Feature
        self.click(application_alerts.alert_btn)
        self.alert_notifi_type(application_alerts.type_loc,type_value1)
        self.alert_notifi_server(application_alerts.server_loc,server_value1)
        self.alert_notifi_app(application_alerts.application_loc,app_value1)
        self.send_data(application_alerts.alertname_loc,alert_name1)
        self.send_data(application_alerts.triggercount_loc,trigger_count1)

        self.alert_notifi_propertyname(application_alerts.alertprop_loc,property_name1)
        self.alert_evalution_period(application_alerts.evalution_period,period1)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc,threshold1)
        self.send_data(application_alerts.alert_appname_loc,alert_appname1)
        self.send_data(application_alerts.status_code,status_code)
        self.send_data(application_alerts.api_path_loc, api_path)

        self.alert_notifi_severity(application_alerts.severity_loc, severity1)
        self.alert_notifi_category(application_alerts.category_loc,alert_category1)
        self.send_data(application_alerts.emailreceiptents_loc, email1)
        self.send_data(application_alerts.phonenumbers_loc, phone_no1)
        sleep(1)


        #Add Alert:
        self.scroll(application_alerts.add_alert)
        sleep(1)
        self.click(application_alerts.add_alert)
        sleep(1)
        self.alert_notifi_type(application_alerts.type_loc, type_value2)
        sleep(1)
        self.alert_notifi_server(application_alerts.server_loc, server_value2)
        sleep(1)
        self.alert_notifi_app(application_alerts.application_loc, app_value2)
        self.send_data(application_alerts.alertname_loc, alert_name2)
        self.send_data(application_alerts.triggercount_loc, trigger_count2)
        self.alert_notifi_propertyname(application_alerts.alertprop_loc, property_name2)
        self.alert_evalution_period(application_alerts.evalution_period, period2)
        self.clear(application_alerts.threshold_loc)
        self.send_data(application_alerts.threshold_loc, threshold2)
        self.send_data(application_alerts.alert_appname_loc, alert_appname2)
        self.send_data(application_alerts.latency_bucket_loc, latency_bucket2)

        self.alert_notifi_severity(application_alerts.severity_loc, severity2)
        self.alert_notifi_category(application_alerts.category_loc, alert_category2)
        self.send_data(application_alerts.emailreceiptents_loc, email2)
        self.send_data(application_alerts.phonenumbers_loc, phone_no2)

        #Submitting Multiple Alerts:
        self.scroll(application_alerts.alert_accept)
        self.click(application_alerts.alert_accept)
        sleep(1)


    #Multiple Alert_Rules FEATURE Alerts:
    def Alert_Rules_multi_app_alert(self, type_value1, server_value1, app_value1, alert_name1,
                                    trigger_count1, property_name1, period1, threshold1, alert_appname1,
                                    latency_bucket1, severity1, alert_category1, email1, phone_no1,
                                    type_value2, server_value2, app_value2, alert_name2,
                                    trigger_count2, property_name2, period2, threshold2, alert_appname2,
                                    latency_bucket2, severity2, alert_category2, email2, phone_no2
                                    ):
        self.zoomout()
        self.click(alert_rules.alert_notifi_locator)
        self.click(alert_rules.alert_rules_feature)  # Clicking on Application Feature
        self.click(alert_rules.alert_btn)
        self.alert_notifi_type(alert_rules.type_loc, type_value1)
        self.alert_notifi_server(alert_rules.server_loc, server_value1)
        self.alert_notifi_app(alert_rules.application_loc, app_value1)
        self.send_data(alert_rules.alertname_loc, alert_name1)
        self.send_data(alert_rules.triggercount_loc, trigger_count1)
        self.alert_notifi_propertyname(alert_rules.alertprop_loc, property_name1)
        self.alert_evalution_period(alert_rules.evalution_period, period1)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc, threshold1)
        self.send_data(alert_rules.alert_appname_loc, alert_appname1)
        self.send_data(alert_rules.latency_bucket_loc, latency_bucket1)

        self.alert_notifi_severity(alert_rules.severity_loc, severity1)
        self.alert_notifi_category(alert_rules.category_loc, alert_category1)
        self.send_data(alert_rules.emailreceiptents_loc, email1)
        self.send_data(alert_rules.phonenumbers_loc, phone_no1)

        # Adding Second Alert:
        self.scroll(alert_rules.add_alert)
        sleep(1)
        self.click(alert_rules.add_alert)
        sleep(1)
        self.alert_notifi_type(alert_rules.type_loc, type_value2)
        self.alert_notifi_server(alert_rules.server_loc, server_value2)
        self.alert_notifi_app(alert_rules.application_loc, app_value2)
        self.send_data(alert_rules.alertname_loc, alert_name2)
        self.send_data(alert_rules.triggercount_loc, trigger_count2)
        self.alert_notifi_propertyname(alert_rules.alertprop_loc, property_name2)
        self.alert_evalution_period(alert_rules.evalution_period, period2)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc, threshold2)

        # If user try to create with Metrics alert the below code not required
        # self.send_data(alert_rules.alert_appname_loc,alert_appname2)
        # self.send_data(alert_rules.latency_bucket_loc, latency_bucket2)

        self.alert_notifi_severity(alert_rules.severity_loc, severity2)
        self.alert_notifi_category(alert_rules.category_loc, alert_category2)
        self.send_data(alert_rules.emailreceiptents_loc, email2)
        self.send_data(alert_rules.phonenumbers_loc, phone_no2)

        # submit Alerts:
        self.scroll(alert_rules.alert_accept)
        self.click(alert_rules.alert_accept)

    def Alert_Rules_multi_metrics_alert(self, type_value1, server_value1, app_value1,
                                        alert_name1, trigger_count1, property_name1, period1, threshold1,
                                        severity1, alert_category1, email1, phone_no1,
                                        type_value2, server_value2, app_value2, alert_name2, trigger_count2,
                                        property_name2, period2, threshold2, alert_appname2, api_path, status_code,
                                        severity2, alert_category2, email2, phone_no2
                                        ):
        self.zoomout()
        self.click(alert_rules.alert_notifi_locator)
        self.click(alert_rules.alert_rules_feature)  # Clicking on Application Feature
        self.click(alert_rules.alert_btn)
        self.alert_notifi_type(alert_rules.type_loc, type_value1)
        self.alert_notifi_server(alert_rules.server_loc, server_value1)
        self.alert_notifi_app(alert_rules.application_loc, app_value1)
        self.send_data(alert_rules.alertname_loc, alert_name1)
        self.send_data(alert_rules.triggercount_loc, trigger_count1)

        self.alert_notifi_propertyname(alert_rules.alertprop_loc, property_name1)
        self.alert_evalution_period(alert_rules.evalution_period, period1)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc, threshold1)

        self.alert_notifi_severity(alert_rules.severity_loc, severity1)
        self.alert_notifi_category(alert_rules.category_loc, alert_category1)
        self.send_data(alert_rules.emailreceiptents_loc, email1)
        self.send_data(alert_rules.phonenumbers_loc, phone_no1)

        # Add Alert:
        self.scroll(alert_rules.add_alert)
        sleep(1)
        self.click(alert_rules.add_alert)
        sleep(1)
        self.alert_notifi_type(alert_rules.type_loc, type_value2)
        self.alert_notifi_server(alert_rules.server_loc, server_value2)
        self.alert_notifi_app(alert_rules.application_loc, app_value2)
        self.send_data(alert_rules.alertname_loc, alert_name2)
        self.send_data(alert_rules.triggercount_loc, trigger_count2)

        self.alert_notifi_propertyname(alert_rules.alertprop_loc, property_name2)
        self.alert_evalution_period(alert_rules.evalution_period, period2)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc, threshold2)
        self.send_data(alert_rules.alert_appname_loc, alert_appname2)
        self.send_data(alert_rules.status_code, status_code)
        self.send_data(alert_rules.api_path_loc, api_path)

        self.alert_notifi_severity(alert_rules.severity_loc, severity2)
        self.alert_notifi_category(alert_rules.category_loc, alert_category2)
        self.send_data(alert_rules.emailreceiptents_loc, email2)
        self.send_data(alert_rules.phonenumbers_loc, phone_no2)

        # Submitting Multiple Alerts:
        self.scroll(alert_rules.alert_accept)
        self.click(alert_rules.alert_accept)

    def Alert_Rules_multi_API_alert(self, type_value1, server_value1, app_value1, alert_name1, trigger_count1,
                                    property_name1,
                                    period1, threshold1, alert_appname1, api_path, status_code, severity1,
                                    alert_category1, email1, phone_no1,
                                    type_value2, server_value2, app_value2, alert_name2,
                                    trigger_count2, property_name2, period2, threshold2, alert_appname2,
                                    latency_bucket2, severity2, alert_category2, email2, phone_no2
                                    ):
        self.zoomout()
        self.click(alert_rules.alert_notifi_locator)
        self.click(alert_rules.alert_rules_feature)  # Clicking on Application Feature
        self.click(alert_rules.alert_btn)
        self.alert_notifi_type(alert_rules.type_loc, type_value1)
        self.alert_notifi_server(alert_rules.server_loc, server_value1)
        self.alert_notifi_app(alert_rules.application_loc, app_value1)
        self.send_data(alert_rules.alertname_loc, alert_name1)
        self.send_data(alert_rules.triggercount_loc, trigger_count1)

        self.alert_notifi_propertyname(alert_rules.alertprop_loc, property_name1)
        self.alert_evalution_period(alert_rules.evalution_period, period1)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc, threshold1)
        self.send_data(alert_rules.alert_appname_loc, alert_appname1)
        self.send_data(alert_rules.status_code, status_code)
        self.send_data(alert_rules.api_path_loc, api_path)

        self.alert_notifi_severity(alert_rules.severity_loc, severity1)
        self.alert_notifi_category(alert_rules.category_loc, alert_category1)
        self.send_data(alert_rules.emailreceiptents_loc, email1)
        self.send_data(alert_rules.phonenumbers_loc, phone_no1)
        sleep(1)

        # Add Alert:
        self.scroll(alert_rules.add_alert)
        sleep(1)
        self.click(alert_rules.add_alert)
        sleep(1)
        self.alert_notifi_type(alert_rules.type_loc, type_value2)
        sleep(1)
        self.alert_notifi_server(alert_rules.server_loc, server_value2)
        sleep(1)
        self.alert_notifi_app(alert_rules.application_loc, app_value2)
        self.send_data(alert_rules.alertname_loc, alert_name2)
        self.send_data(alert_rules.triggercount_loc, trigger_count2)
        self.alert_notifi_propertyname(alert_rules.alertprop_loc, property_name2)
        self.alert_evalution_period(alert_rules.evalution_period, period2)
        self.clear(alert_rules.threshold_loc)
        self.send_data(alert_rules.threshold_loc, threshold2)
        self.send_data(alert_rules.alert_appname_loc, alert_appname2)
        self.send_data(alert_rules.latency_bucket_loc, latency_bucket2)

        self.alert_notifi_severity(alert_rules.severity_loc, severity2)
        self.alert_notifi_category(alert_rules.category_loc, alert_category2)
        self.send_data(alert_rules.emailreceiptents_loc, email2)
        self.send_data(alert_rules.phonenumbers_loc, phone_no2)

        # Submitting Multiple Alerts:
        self.scroll(alert_rules.alert_accept)
        self.click(alert_rules.alert_accept)
        sleep(1)





