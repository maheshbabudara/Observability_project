class External_module:
    external_tools=('xpath','//div[@class="LogoHeading"]/h1[text()="External Tools"]')

    Add_external_config=('xpath','//button[contains(text(),"Add External Config")]')

    #Basic Configuration:
    integration_name=('xpath','//label[contains(text(),"Integration Name")]/following-sibling::input[@formcontrolname="integrationName"]')
    Tool_type=('xpath','//label[contains(text(),"Tool Type")]/following-sibling::select[@formcontrolname="toolType"]')
    environment=('xpath','//label[contains(text(),"Environment")]/following-sibling::select[@formcontrolname="environment"]')
    config_version=('xpath','//label[contains(text(),"Config Version")]/following-sibling::input[@formcontrolname="configVersion"]')

    #Configuration:
    Host=('xpath','//label[contains(text(),"Host")]/following-sibling::input[@formcontrolname="host"]')
    Port=('xpath','//label[contains(text(),"Port")]/following-sibling::input[@formcontrolname="port"]')
    Protocol=('xpath','//label[contains(text(),"Protocol")]/following-sibling::select[@formcontrolname="protocol"]')
    Auth_Type=('xpath','//label[contains(text(),"Auth Type")]/following-sibling::select[@formcontrolname="authType"]')
    username=('xpath','//label[contains(text(),"Username")]/following-sibling::input[@formcontrolname="username"]')
    password=('xpath','//label[contains(text(),"Password")]/following-sibling::input[@formcontrolname="password"]')
    index_pattern=('xpath','//label[contains(text(),"Index Pattern")]/following-sibling::input[@formcontrolname="indexPattern"]')
    timeout=('xpath','//label[contains(text(),"Timeout")]/following-sibling::input[@formcontrolname="timeout"]')
    apikey=('xpath','//label[contains(text(),"API Key")]/following-sibling::input[@formcontrolname="apiKey"]')

    save_btn=('xpath','//button[@class="save-btn"]')
    cancel_btn=('xpath','//button[@class="cancel-btn" and contains(text(),"Cancel")]')

    #Deletion Locators:
    delete_btn=('xpath','//button[@class="delete-confirm-btn"]')
    cancel_delete=('xpath','//button[@class="cancel-btn"]')

    #View Loactors:
    integration_heading=('xpath','//span[@class="label" and text()="Integration Name:"]')
    integration_value=('xpath','//span[@class="label" and text()="Integration Name:"]/following-sibling::span[@class="value"]')
    Tool_type_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Tool Type:"]')
    Tool_type_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Tool Type:"]/following-sibling::span[@class="value"]')
    Environment_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Environment:"]')
    Environment_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Environment:"]/following-sibling::span[@class="value"]')

    #connection configuration:
    Host_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Host:"]')
    Host_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Host:"]/following-sibling::span[@class="value"]')
    Port_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Port:"]')
    Port_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Port:"]/following-sibling::span[@class="value"]')
    Protocol_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Protocol:"]')
    Protocol_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Protocol:"]/following-sibling::span[@class="value"]')
    Auth_type_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Auth Type:"]')
    Auth_type_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Auth Type:"]/following-sibling::span[@class="value"]')
    Timeout_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Timeout (ms):"]')
    Timeout_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Timeout (ms):"]/following-sibling::span[@class="value"]')
    created_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Created:"]')
    created_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Created:"]/following-sibling::span[@class="value"]')
    Last_updated_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Last Updated:"]')
    Last_updated_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Last Updated:"]/following-sibling::span[@class="value"]')
    status_heading=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Status:"]')
    status_value=('xpath','//div[@class="view-config-content"]//span[@class="label" and text()="Status:"]/following-sibling::span[@class="value active"]')







