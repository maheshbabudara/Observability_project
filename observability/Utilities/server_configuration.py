class server_config:
    server_configuration=('xpath','//div[@class="LogoHeading"]/h1[text()="Server Configuration"]')
    add_server=('xpath','//button[contains(text(),"Add Server")]')
    #server Locators:
    server_name=('xpath','//label[starts-with(text(),"Server Name")]/following-sibling::input[@formcontrolname="serverName"]')
    ipaddress=('xpath','//label[starts-with(text(),"IP Address ")]/following-sibling::input[@formcontrolname="ipAddress"]')
    port=('xpath','//label[starts-with(text(),"Port")]/following-sibling::input[@formcontrolname="environment"]')
    os=('xpath','//label[starts-with(text(),"Operating System")]/following-sibling::input[@formcontrolname="operatingSystem"]')
    server_owner=('xpath','//label[starts-with(text(),"Server Owner")]/following-sibling::select[@formcontrolname="serverOwner"]')
    phone_number=('xpath','//label[starts-with(text(),"Phone Number")]/following-sibling::input[@formcontrolname="phoneNumber"]')
    #Agent Locators:
    agent_name=('xpath','//label[starts-with(text(),"Agent Name")]/following-sibling::input[@formcontrolname="agentName"]')
    agent_ip=('xpath','//label[starts-with(text(),"Agent IP")]/following-sibling::input[@formcontrolname="agentIp"]')
    agen_port=('xpath','//label[starts-with(text(),"Agent Port")]/following-sibling::input[@formcontrolname="agentPort"]')

    metrics=('xpath','//label[starts-with(text(),"Metrics")]/following-sibling::input[@formcontrolname="metrics"]')
    logs=('xpath','//label[starts-with(text(),"Logs")]/following-sibling::input[@formcontrolname="logs"]')
    traces=('xpath','//label[starts-with(text(),"Traces")]/following-sibling::input[@formcontrolname="traces"]')

    #Log section Locators:
    path=('xpath','//label[starts-with(text(),"Path")]/following-sibling::input[@placeholder="Enter log path"]')
    Name=('xpath','//label[starts-with(text(),"Name")]/following-sibling::input[@placeholder="Enter log name"]')
    description=('xpath','//label[starts-with(text(),"Description")]/following-sibling::input[@placeholder="Enter description"]')
    application=('xpath','//label[starts-with(text(),"Application")]/following-sibling::input[@placeholder="Enter application name"]')

    #Run Time Environment:
    docker=('xpath','//label[text()="Docker"]/preceding-sibling::input[@formcontrolname="runtimeDocker"]')
    kubernetes=('xpath','//label[text()="Kubernetes"]/preceding-sibling::input[@formcontrolname="runtimeKubernetes"]')
    baremetal=('xpath','//label[text()="Baremetal"]/preceding-sibling::input[@formcontrolname="runtimeBaremetal"]')

    #Docker Locators:
    container_name=('xpath','//label[text()="Container Name"]/following-sibling::input')
    container_id=('xpath','//label[text()="Container ID"]/following-sibling::input')

    #Kubernetes Locators:
    cluster_name=('xpath','//label[text()="Cluster Name"]/following-sibling::input[@name="kubernetesClusterName"]')
    name_spaces=('xpath','//label[text()="Namespace"]/following-sibling::input')


    #consent
    consent_checkbox=('xpath','//input[@id="consentCheckbox"]')

    save_btn=('xpath','//button[@class="save-btn"]/span')

    #Edit locator:
    edit_btn=('xpath','//tr[@class="ng-star-inserted"]//a[text()=" docker_kuber_bare creation "]/../following-sibling::td//button[@title="Edit"]')
    delete_btn=('xpath','//tr[@class="ng-star-inserted"]//a[text()=" docker_kuber_bare creation "]/../following-sibling::td//button[@title="Delete"]')
    yes_delete_btn=('xpath','//button[@class="btn btn-danger" and contains(text(),"Yes, Delete")]')
    cancel_btn=('xpath','//button[text()="Cancel"]')



