from Library.library import Base
from time import sleep
from Utilities.server_configuration import server_config
from Utilities.server_monitoring_locators import server


class server_configuration(Base):
    def docker(self, server_name,ipaddress,port,os,owner,
               phn_no,agent_name,agent_ip,agen_port,path,
               Name,description,application,container_name,
               container_id,):
        self.zoomout()
        self.click(server_config.server_configuration)
        self.click(server_config.add_server)
        #server details:
        self.send_data(server_config.server_name,server_name)
        self.send_data(server_config.ipaddress,ipaddress)
        self.send_data(server_config.port,port)
        self.send_data(server_config.os,os)
        self.server_owner(server_config.server_owner,owner)
        self.send_data(server_config.phone_number,phn_no)
        self.send_data(server_config.agent_name,agent_name)
        self.send_data(server_config.agent_ip, agent_ip)
        self.send_data(server_config.agen_port,agen_port)
        self.dynamic_click(server_config.metrics)
        self.dynamic_click(server_config.logs)
        self.dynamic_click(server_config.traces)
        #Logs:
        self.send_data(server_config.path, path)
        self.send_data(server_config.Name, Name)
        self.send_data(server_config.description,description)
        self.send_data(server_config.application,application)
        #Docker checkbox:
        self.dynamic_click(server_config.docker)
        #Entering Docker details:
        self.send_data(server_config.container_name,container_name)
        self.send_data(server_config.container_id,container_id)
        #consent check:
        self.dynamic_click(server_config.consent_checkbox)
        #saving:
        self.dynamic_click(server_config.save_btn)

    def kubernetes(self, server_name,ipaddress,port,os,owner,
               phn_no,agent_name,agent_ip,agen_port,path,
               Name,description,application,cluster_name,
               name_spaces,):
        self.zoomout()
        self.click(server_config.server_configuration)
        self.click(server_config.add_server)
        #server details:
        self.send_data(server_config.server_name,server_name)
        self.send_data(server_config.ipaddress,ipaddress)
        self.send_data(server_config.port,port)
        self.send_data(server_config.os,os)
        self.server_owner(server_config.server_owner,owner)
        self.send_data(server_config.phone_number,phn_no)
        self.send_data(server_config.agent_name,agent_name)
        self.send_data(server_config.agent_ip, agent_ip)
        self.send_data(server_config.agen_port,agen_port)
        self.dynamic_click(server_config.metrics)
        self.dynamic_click(server_config.logs)
        self.dynamic_click(server_config.traces)
        #Logs:
        self.send_data(server_config.path, path)
        self.send_data(server_config.Name, Name)
        self.send_data(server_config.description,description)
        self.send_data(server_config.application,application)
        #kubernetes checkbox:
        self.dynamic_click(server_config.kubernetes)
        #Entering Kubernetes details:
        self.send_data(server_config.cluster_name,cluster_name)
        self.send_data(server_config.name_spaces,name_spaces)
        #consent check:
        self.dynamic_click(server_config.consent_checkbox)
        #saving:
        self.dynamic_click(server_config.save_btn)

    def Baremetal(self, server_name,ipaddress,port,os,owner,
               phn_no,agent_name,agent_ip,agen_port,path,
               Name,description,application):
        self.zoomout()
        self.click(server_config.server_configuration)
        self.click(server_config.add_server)
        #server details:
        self.send_data(server_config.server_name,server_name)
        self.send_data(server_config.ipaddress,ipaddress)
        self.send_data(server_config.port,port)
        self.send_data(server_config.os,os)
        self.server_owner(server_config.server_owner,owner)
        self.send_data(server_config.phone_number,phn_no)
        self.send_data(server_config.agent_name,agent_name)
        self.send_data(server_config.agent_ip, agent_ip)
        self.send_data(server_config.agen_port,agen_port)
        self.dynamic_click(server_config.metrics)
        self.dynamic_click(server_config.logs)
        self.dynamic_click(server_config.traces)
        #Logs:
        self.send_data(server_config.path, path)
        self.send_data(server_config.Name, Name)
        self.send_data(server_config.description,description)
        self.send_data(server_config.application,application)
        #Baremetal check:
        self.dynamic_click(server_config.baremetal)
        #consent check:
        self.dynamic_click(server_config.consent_checkbox)
        #saving:
        self.dynamic_click(server_config.save_btn)

    def all_types(self, server_name, ipaddress, port, os, owner,
                  phn_no, agent_name, agent_ip, agen_port, path,
                  Name, description, application, container_name,
                  container_id, cluster_name, name_spaces):
        self.zoomout()
        self.click(server_config.server_configuration)
        self.click(server_config.add_server)
        #server details:
        self.send_data(server_config.server_name,server_name)
        self.send_data(server_config.ipaddress,ipaddress)
        self.send_data(server_config.port,port)
        self.send_data(server_config.os,os)
        self.server_owner(server_config.server_owner,owner)
        self.send_data(server_config.phone_number,phn_no)
        self.send_data(server_config.agent_name,agent_name)
        self.send_data(server_config.agent_ip, agent_ip)
        self.send_data(server_config.agen_port,agen_port)
        self.dynamic_click(server_config.metrics)
        self.dynamic_click(server_config.logs)
        self.dynamic_click(server_config.traces)
        #Logs:
        self.send_data(server_config.path, path)
        self.send_data(server_config.Name, Name)
        self.send_data(server_config.description,description)
        self.send_data(server_config.application,application)
        #Docker checkbox:
        self.dynamic_click(server_config.docker)
        #Entering Docker details:
        self.send_data(server_config.container_name,container_name)
        self.send_data(server_config.container_id,container_id)
        #kubernetes checkbox:
        self.dynamic_click(server_config.kubernetes)
        #Entering Kubernetes details:
        self.send_data(server_config.cluster_name,cluster_name)
        self.send_data(server_config.name_spaces,name_spaces)
        #Baremetal check:
        self.dynamic_click(server_config.baremetal)
        #consent check:
        self.dynamic_click(server_config.consent_checkbox)
        #saving:
        self.dynamic_click(server_config.save_btn)

    def docker_edit(self, server_name,new_server_name, ipaddress, port, os, owner,
                    phn_no, agent_name, agent_ip, agen_port, path,
                    Name, description, application, container_name,
                    container_id, cluster_name, name_spaces):
        self.zoomout()
        self.click(server_config.server_configuration)
        edit_btn = ('xpath',
                    f'//a[text()=" {server_name} "]/../following-sibling::td//button[@title="Edit"]')
        self.click(edit_btn)
        sleep(1)
        #server details:
        self.clear(server_config.server_name) #Clearing server name
        self.send_data(server_config.server_name,new_server_name)
        self.clear(server_config.ipaddress) #Clearing server ip address
        self.send_data(server_config.ipaddress,ipaddress)
        self.clear(server_config.port)  # Clearing server port
        self.send_data(server_config.port,port)
        self.clear(server_config.os)  # Clearing server os
        self.send_data(server_config.os,os)
        self.server_owner(server_config.server_owner,owner)
        self.clear(server_config.phone_number)  # Clearing server Phone Number
        self.send_data(server_config.phone_number,phn_no)
        self.clear(server_config.agent_name)  # Clearing server agent name
        self.send_data(server_config.agent_name,agent_name)
        self.clear(server_config.agent_ip)  # Clearing server agent ip
        self.send_data(server_config.agent_ip, agent_ip)
        self.clear(server_config.agen_port)  # Clearing server agent port
        self.send_data(server_config.agen_port,agen_port)
        self.dynamic_click(server_config.metrics)  #unchecking metrics
        # self.dynamic_click(server_config.logs)
        self.dynamic_click(server_config.traces)   #unchecking Traces
        #Logs:
        self.clear(server_config.path)  # Clearing server agent path
        self.send_data(server_config.path, path)
        self.send_data(server_config.Name, Name)
        self.send_data(server_config.description,description)
        self.clear(server_config.application)  # Clearing server application
        self.send_data(server_config.application,application)

        #Docker checkbox:
        self.dynamic_click(server_config.docker)  #Unchecking docker
        #Entering Docker details:
        self.send_data(server_config.container_name,container_name)
        self.send_data(server_config.container_id,container_id)

        # kubernetes checkbox:
        self.dynamic_click(server_config.kubernetes)
        # Entering Kubernetes details:
        self.clear(server_config.cluster_name)  # Clearing server cluster name
        self.send_data(server_config.cluster_name, cluster_name)
        self.clear(server_config.name_spaces)  # Clearing server name spaces
        self.send_data(server_config.name_spaces, name_spaces)

        #consent check:
        self.dynamic_click(server_config.consent_checkbox)
        #saving:
        self.dynamic_click(server_config.save_btn)

    def kubernetes_edit(self, server_name,new_server_name, ipaddress, port, os, owner,
                    phn_no, agent_name, agent_ip, agen_port, path,
                    Name, description, application, cluster_name, name_spaces,
                    container_name,container_id, ):
        self.zoomout()
        self.click(server_config.server_configuration)
        edit_btn = ('xpath',
                    f'//a[text()=" {server_name} "]/../following-sibling::td//button[@title="Edit"]')
        self.click(edit_btn)
        sleep(1)
        #server details:
        self.clear(server_config.server_name) #Clearing server name
        self.send_data(server_config.server_name,new_server_name)
        self.clear(server_config.ipaddress) #Clearing server ip address
        self.send_data(server_config.ipaddress,ipaddress)
        self.clear(server_config.port)  # Clearing server port
        self.send_data(server_config.port,port)
        self.clear(server_config.os)  # Clearing server os
        self.send_data(server_config.os,os)
        self.server_owner(server_config.server_owner,owner)
        self.clear(server_config.phone_number)  # Clearing server Phone Number
        self.send_data(server_config.phone_number,phn_no)
        self.clear(server_config.agent_name)  # Clearing server agent name
        self.send_data(server_config.agent_name,agent_name)
        self.clear(server_config.agent_ip)  # Clearing server agent ip
        self.send_data(server_config.agent_ip, agent_ip)
        self.clear(server_config.agen_port)  # Clearing server agent port
        self.send_data(server_config.agen_port,agen_port)
        self.dynamic_click(server_config.metrics)  #unchecking metrics
        # self.dynamic_click(server_config.logs)
        self.dynamic_click(server_config.traces)   #unchecking Traces
        #Logs:
        self.clear(server_config.path)  # Clearing server agent path
        self.send_data(server_config.path, path)
        self.send_data(server_config.Name, Name)
        self.send_data(server_config.description,description)
        self.clear(server_config.application)  # Clearing server application
        self.send_data(server_config.application,application)

        # kubernetes checkbox:
        self.dynamic_click(server_config.kubernetes)  #Unchecking kubernetes
        # Entering Kubernetes details:
        self.clear(server_config.cluster_name)  # Clearing server cluster name
        self.send_data(server_config.cluster_name, cluster_name)
        self.clear(server_config.name_spaces)  # Clearing server name spaces
        self.send_data(server_config.name_spaces, name_spaces)

        #Docker checkbox:
        self.dynamic_click(server_config.docker) #checking Docker
        #Entering Docker details:
        self.clear(server_config.container_name) # Clearing server container name
        self.send_data(server_config.container_name,container_name)
        self.clear(server_config.container_id)  # Clearing server container id
        self.send_data(server_config.container_id,container_id)

        #consent check:
        self.dynamic_click(server_config.consent_checkbox)
        #saving:
        self.dynamic_click(server_config.save_btn)

    def Baremetal_edit(self, server_name,new_server_name, ipaddress, port, os, owner,
                    phn_no, agent_name, agent_ip, agen_port, path,
                    Name, description, application, cluster_name, name_spaces,
                    container_name,container_id, ):
        self.zoomout()
        self.click(server_config.server_configuration)
        edit_btn = ('xpath',
                    f'//a[text()=" {server_name} "]/../following-sibling::td//button[@title="Edit"]')
        self.click(edit_btn)
        sleep(1)
        #server details:
        self.clear(server_config.server_name) #Clearing server name
        self.send_data(server_config.server_name,new_server_name)
        self.clear(server_config.ipaddress) #Clearing server ip address
        self.send_data(server_config.ipaddress,ipaddress)
        self.clear(server_config.port)  # Clearing server port
        self.send_data(server_config.port,port)
        self.clear(server_config.os)  # Clearing server os
        self.send_data(server_config.os,os)
        self.server_owner(server_config.server_owner,owner)
        self.clear(server_config.phone_number)  # Clearing server Phone Number
        self.send_data(server_config.phone_number,phn_no)
        self.clear(server_config.agent_name)  # Clearing server agent name
        self.send_data(server_config.agent_name,agent_name)
        self.clear(server_config.agent_ip)  # Clearing server agent ip
        self.send_data(server_config.agent_ip, agent_ip)
        self.clear(server_config.agen_port)  # Clearing server agent port
        self.send_data(server_config.agen_port,agen_port)
        self.dynamic_click(server_config.metrics)  #unchecking metrics
        # self.dynamic_click(server_config.logs)
        self.dynamic_click(server_config.traces)   #unchecking Traces
        #Logs:
        self.clear(server_config.path)  # Clearing server agent path
        self.send_data(server_config.path, path)
        self.send_data(server_config.Name, Name)
        self.send_data(server_config.description,description)
        self.clear(server_config.application)  # Clearing server application
        self.send_data(server_config.application,application)

        # kubernetes checkbox:
        self.dynamic_click(server_config.kubernetes)  #Unchecking kubernetes
        # Entering Kubernetes details:
        self.clear(server_config.cluster_name)  # Clearing server cluster name
        self.send_data(server_config.cluster_name, cluster_name)
        self.clear(server_config.name_spaces)  # Clearing server name spaces
        self.send_data(server_config.name_spaces, name_spaces)

        #Docker checkbox:
        self.dynamic_click(server_config.docker) #Unchecking Docker
        #Entering Docker details:
        self.clear(server_config.container_name) # Clearing server container name
        self.send_data(server_config.container_name,container_name)
        self.clear(server_config.container_id)  # Clearing server container id
        self.send_data(server_config.container_id,container_id)

        #Baremetal check:
        self.dynamic_click(server_config.baremetal)    #changing to Barmetal from docker & Kubernetes

        #consent check:
        self.dynamic_click(server_config.consent_checkbox)
        #saving:
        self.dynamic_click(server_config.save_btn)


    def delete_server(self, server_name):
        self.zoomout()
        self.click(server_config.server_configuration)
        delete_btn = ('xpath',
                    f'//a[text()=" {server_name} "]/../following-sibling::td//button[@title="Delete"]')
        self.click(delete_btn)
        sleep(1)
        self.click(server_config.yes_delete_btn)







