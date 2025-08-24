from time import sleep
from Library.library import Base
from Utilities.External_tools import External_module

class external_tools(Base):
    # External Tools with BASIC AUTH:
    def Basic_auth(self, integration_name,tools,environment,
                 config_version,host,port,protocol,auth_Type,
                 username,password,index_pattern,timeout):
        self.zoomout()
        self.click(External_module.external_tools)
        self.click(External_module.Add_external_config)
        #Basic configuration:
        self.send_data(External_module.integration_name, integration_name)
        self.tools_type(External_module.Tool_type,tools)
        self.environment(External_module.environment, environment)
        self.send_data(External_module.config_version, config_version)
        #Configuration:
        self.send_data(External_module.Host,host)
        self.send_data(External_module.Port,port)
        self.protocol(External_module.Protocol,protocol)
        self.Auth_type(External_module.Auth_Type,auth_Type)
        self.send_data(External_module.username,username)
        self.send_data(External_module.password,password)
        self.send_data(External_module.index_pattern,index_pattern)
        self.clear(External_module.timeout)
        self.send_data(External_module.timeout,timeout)
        sleep(1)
        self.click(External_module.save_btn)

    #External Tools with API KEY AUTH:
    def API_auth(self, integration_name,tools,environment,
                 config_version,host,port,protocol,auth_Type,
                 apikey,index_pattern,timeout):
        self.zoomout()
        self.click(External_module.external_tools)
        self.click(External_module.Add_external_config)
        #Basic configuration:
        self.send_data(External_module.integration_name, integration_name)
        self.tools_type(External_module.Tool_type,tools)
        self.environment(External_module.environment, environment)
        self.send_data(External_module.config_version, config_version)
        #Configuration:
        self.send_data(External_module.Host,host)
        self.send_data(External_module.Port,port)
        self.protocol(External_module.Protocol,protocol)
        self.Auth_type(External_module.Auth_Type,auth_Type)
        self.send_data(External_module.apikey,apikey)
        self.send_data(External_module.index_pattern,index_pattern)
        self.clear(External_module.timeout)
        self.send_data(External_module.timeout,timeout)
        sleep(1)
        self.click(External_module.save_btn)

    #Deletion of External Tools:
    def delete(self,Tool_name):
        self.zoomout()
        self.click(External_module.external_tools)
        record_delete=('xpath',
                       f'//div[@class="config-header"]/h3[text()="{Tool_name}"]/../following-sibling::div[@class="config-footer"]//button[@class="delete-btn"]')
        # sleep(1)
        self.dynamic_click(record_delete)
        self.click(External_module.delete_btn)

    #Viewing and Appending the details of External Tools:
    def view(self,Tool_name):
        self.zoomout()
        self.click(External_module.external_tools)
        record_delete=('xpath',
                       f'//div[@class="config-header"]/h3[text()="{Tool_name}"]/../following-sibling::div[@class="config-footer"]//button[@class="view-btn"]')
        # sleep(1)
        self.dynamic_click(record_delete)

        details={
            "Basic configuration Details":[
                (External_module.integration_heading, External_module.integration_value),
                (External_module.Tool_type_heading, External_module.Tool_type_value),
                (External_module.Environment_heading, External_module.Environment_value),
            ],
            "Connection configuration Details":[
                (External_module.Host_heading, External_module.Host_value),
                (External_module.Port_heading, External_module.Port_value),
                (External_module.Protocol_heading, External_module.Protocol_value),
                (External_module.Auth_type_heading, External_module.Auth_type_value),
                (External_module.Timeout_heading, External_module.Timeout_value),
            ],
            "Metadata Details":[
                (External_module.created_heading, External_module.created_value),
                (External_module.Last_updated_heading, External_module.Last_updated_value),
                (External_module.status_heading, External_module.status_value),
            ]
        }
        with open('Desired External_tool Details.txt', 'a', encoding="utf-8") as file:
            file.write(f"{'*'*100}\n")
            file.write(f"Desired External_tool - {Tool_name} Details\n\n")
            for section,pairs in details.items():
                file.write(f"{section}:\n") #Writing sections:
                for heading_locator,value_locator in pairs:  #using locators
                    heading=self.search_element(heading_locator).text
                    value=self.search_element(value_locator).text
                    file.write(f"{heading} - {value}\n")  #appending values of web elements
                #Extra spaces between sections:
                file.write(f"\n")









