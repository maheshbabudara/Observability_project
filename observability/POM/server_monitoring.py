from dataclasses import field

from Library.library import Base
from Utilities.server_monitoring_locators import server

from time import sleep
class server_monitor(Base):
    def server_mon1(self,server_name):
        self.zoomout()
        self.click(server.server_monitoring_module)
        sleep(1)
        self.server_selection(server.servers_dropdown,server_name)
        sleep(10)

        with open('server_details.txt', "a", encoding="utf-8") as file:
            file.write(f"\n{'#' * 100}\n")
            file.write(f"Server Name: {server_name}\n")
            file.write(f"{'-' * 50}\n")

            # # Application Health details
            # file.write(f"\n{'*' * 20} Application details {'*' * 20}\n\n")
            # App_health = self.search_element(server.application_health_heading)
            # file.write(f"{App_health.text}:\n")
            # Health_value = self.search_element(server.application_health_value)
            # file.write(f"{Health_value.text}\n")
            #
            # # Service Availability
            # service_avail = self.search_element(server.server_availability_heading)
            # file.write(f"{service_avail.text}:\n")
            # service_value = self.search_element(server.server_availability_value)
            # file.write(f"{service_value.text}\n")
            #
            # # No of Restarts
            # restart_heading = self.search_element(server.No_of_restarts_heading)
            # file.write(f"{restart_heading.text}:\n")
            # restart_value = self.search_element(server.No_of_restarts_value)
            # file.write(f"{restart_value.text}\n")
            #
            # # No of Pods
            # Pods_heading = self.search_element(server.No_of_pods_heading)
            # file.write(f"{Pods_heading.text}:\n")
            # Pods_value = self.search_element(server.No_of_pods_value)
            # file.write(f"{Pods_value.text}\n")

            # CPU
            file.write(f"\n{'*' * 20} Server Metrics {'*' * 20}\n\n")
            cpu = self.search_element(server.CPU_heading)
            file.write(f"{cpu.text}:\n")
            cpu_percent = self.search_element(server.CPU_percentage)
            file.write(f"{cpu_percent.text}\n")
            cpu_cores = self.search_element(server.CPU_cores)
            file.write(f"({cpu_cores.text})\n")

            # Memory
            memory_heading = self.search_element(server.Memory_heading)
            file.write(f"{memory_heading.text}:\n")
            memory_percent = self.search_element(server.Memory_percentage)
            file.write(f"{memory_percent.text}\n")
            memory_gb = self.search_element(server.Memory_GB)
            file.write(f"({memory_gb.text})\n")

            # Disk
            disk_heading = self.search_element(server.Disk_heading)
            file.write(f"{disk_heading.text}:\n")
            disk_percent = self.search_element(server.Disk_percentage)
            file.write(f"{disk_percent.text}\n")
            disk_gb = self.search_element(server.Disk_GB)
            file.write(f"({disk_gb.text})\n")

            # Network
            network_heading = self.search_element(server.Network_heading)
            file.write(f"{network_heading.text}:\n")
            network_percent = self.search_element(server.Network_percentage)
            file.write(f"{network_percent.text}\n")
            network_ms = self.search_element(server.Network_ms)
            file.write(f"({network_ms.text})\n")

            #Request Volume:
            file.write(f"\n{'*' * 20} API Metrics {'*' * 20}\n\n")
            req_vol_heading=self.search_element(server.Request_vol_heading)
            file.write(f"{req_vol_heading.text}:\n")
            re_vol_value=self.search_element(server.Req_vol_value)
            file.write(f'{re_vol_value.text}\n')

            #Failed Requests:
            failed_req_heading=self.search_element(server.Failed_req_heading)
            file.write(f"{failed_req_heading.text}:\n")
            failed_re_value=self.search_element(server.Failed_req_value)
            file.write(f"{failed_re_value.text}\n")

            #400 Erros:
            client_error_heading=self.search_element(server.client_error_heading)
            file.write(f"{client_error_heading.text}:\n")
            client_error_value=self.search_element(server.client_error_value)
            file.write(f"{client_error_value.text}\n")

            #500 Errors:
            server_error_heading=self.search_element(server.server_error_heading)
            file.write(f"{server_error_heading.text}:\n")
            server_error_value=self.search_element(server.server_error_value)
            file.write(f"{server_error_value.text}\n")

            #succes Rate:
            success_rate_heading=self.search_element(server.success_rate_heading)
            file.write(f"{success_rate_heading.text}:\n")
            success_rate_value=self.search_element(server.sucess_rate_value)
            file.write(f"{success_rate_value.text}\n")

            #Total Logs:
            file.write(f"\n{'*' * 20} Log Monitoring {'*' * 20}\n")
            total_logs_heading=self.search_element(server.Total_logs_heading)
            file.write(f"{total_logs_heading.text}:\n")
            total_logs_value=self.search_element(server.Total_logs_value)
            file.write(f"{total_logs_value.text}\n")

            #Info details:
            info_heading=self.search_element(server.Info_heading)
            file.write(f"{info_heading.text}:\n")
            info_value=self.search_element(server.Info_value)
            file.write(f"{info_value.text}\n")

            #Warning:
            warn_heading=self.search_element(server.Warning_heading)
            file.write(f"{warn_heading.text}:\n")
            warn_value=self.search_element(server.Warning_value)
            file.write(f"{warn_value.text}\n")

            #Error:
            error_heading=self.search_element(server.Error_heading)
            file.write(f"{error_heading.text}:\n")
            error_value=self.search_element(server.Error_value)
            file.write(f"{error_value.text}\n")

            #Debug:
            debug_heading=self.search_element(server.Debug_heading)
            file.write(f"{debug_heading.text}:\n")
            debug_value=self.search_element(server.Debug_value)
            file.write(f"{debug_value.text}\n")



            # #Heap Usage:
            # file.write(f'{'*'*20} JVM-Metrics {"*"*20}')
            # heap_usage_heading=self.search_element(server.Heap_usage_heading)
            # file.write(f"{heap_usage_heading.text}:\n")
            # head_usage_value=self.search_element(server.Heap_usage_value)
            # file.write(f"{head_usage_value.text}\n")
            #
            # #GC Frequency:
            # gc_freq_heading=self.search_element(server.GC_Frequency_heading)
            # file.write(f"{gc_freq_heading.text}:\n")
            # gc_freq_value=self.search_element(server.GC_Frequency_value)
            # file.write(f"{gc_freq_value.text}\n")
            #
            # #Thread Count:
            # head_count_heading=self.search_element(server.Thread_count_heading)
            # file.write(f"{head_count_heading.text}\n")
            # head_count_value=self.search_element(server.Thread_count_value)
            # file.write(f"{head_count_value.text}\n")
            #
            # #CPU Usage:
            # cpu_usage_heading=self.search_element(server.CPU_Usage_heading)
            # file.write(f"{cpu_usage_heading.text}\n")
            # cpu_usage_value=self.search_element(server.CPU_Usage_value)
            # file.write(f"{cpu_usage_value.text}\n")
            #
            # #Memory Usage:
            # memory_usage_heading=self.search_element(server.Memory_usage_heading)
            # file.write(f"{memory_usage_heading.text}:\n")
            # memory_usage_value=self.search_element(server.Memory_usage_value)
            # file.write(f"{memory_usage_value.text}\n")



    def server_mon2(self,server_name):
        self.zoomout()
        self.click(server.server_monitoring_module)
        sleep(1)
        self.server_selection(server.servers_dropdown, server_name)
        sleep(10)

        with open('server_details.txt', "a", encoding="utf-8") as file:
            file.write(f"\n{'#' * 100}\n")
            file.write(f"Server Name: {server_name}\n")
            file.write(f"{'-' * 50}\n")

            # # Application Health details
            # file.write(f"\n{'*' * 20} Application details {'*' * 20}\n\n")
            # App_health = self.search_element(server.application_health_heading)
            # file.write(f"{App_health.text}:\n")
            # Health_value = self.search_element(server.application_health_value)
            # file.write(f"{Health_value.text}\n")
            #
            # # Service Availability
            # service_avail = self.search_element(server.server_availability_heading)
            # file.write(f"{service_avail.text}:\n")
            # service_value = self.search_element(server.server_availability_value)
            # file.write(f"{service_value.text}\n")
            #
            # # No of Restarts
            # restart_heading = self.search_element(server.No_of_restarts_heading)
            # file.write(f"{restart_heading.text}:\n")
            # restart_value = self.search_element(server.No_of_restarts_value)
            # file.write(f"{restart_value.text}\n")
            #
            # # No of Pods
            # Pods_heading = self.search_element(server.No_of_pods_heading)
            # file.write(f"{Pods_heading.text}:\n")
            # Pods_value = self.search_element(server.No_of_pods_value)
            # file.write(f"{Pods_value.text}\n")

            # CPU
            file.write(f"\n{'*' * 20} Server Metrics {'*' * 20}\n\n")
            cpu = self.search_element(server.CPU_heading)
            file.write(f"{cpu.text}:\n")
            cpu_percent = self.search_element(server.CPU_percentage)
            file.write(f"{cpu_percent.text}\n")
            cpu_cores = self.search_element(server.CPU_cores)
            file.write(f"({cpu_cores.text})\n")

            # Memory
            memory_heading = self.search_element(server.Memory_heading)
            file.write(f"{memory_heading.text}:\n")
            memory_percent = self.search_element(server.Memory_percentage)
            file.write(f"{memory_percent.text}\n")
            memory_gb = self.search_element(server.Memory_GB)
            file.write(f"({memory_gb.text})\n")

            # Disk
            disk_heading = self.search_element(server.Disk_heading)
            file.write(f"{disk_heading.text}:\n")
            disk_percent = self.search_element(server.Disk_percentage)
            file.write(f"{disk_percent.text}\n")
            disk_gb = self.search_element(server.Disk_GB)
            file.write(f"({disk_gb.text})\n")

            # Network
            network_heading = self.search_element(server.Network_heading)
            file.write(f"{network_heading.text}:\n")
            network_percent = self.search_element(server.Network_percentage)
            file.write(f"{network_percent.text}\n")
            network_ms = self.search_element(server.Network_ms)
            file.write(f"({network_ms.text})\n")

            # Request Volume:
            file.write(f"\n{'*' * 20} API Metrics {'*' * 20}\n\n")
            req_vol_heading = self.search_element(server.Request_vol_heading)
            file.write(f"{req_vol_heading.text}:\n")
            re_vol_value = self.search_element(server.Req_vol_value)
            file.write(f'{re_vol_value.text}\n')

            # Failed Requests:
            failed_req_heading = self.search_element(server.Failed_req_heading)
            file.write(f"{failed_req_heading.text}:\n")
            failed_re_value = self.search_element(server.Failed_req_value)
            file.write(f"{failed_re_value.text}\n")

            # 400 Erros:
            client_error_heading = self.search_element(server.client_error_heading)
            file.write(f"{client_error_heading.text}:\n")
            client_error_value = self.search_element(server.client_error_value)
            file.write(f"{client_error_value.text}\n")

            # 500 Errors:
            server_error_heading = self.search_element(server.server_error_heading)
            file.write(f"{server_error_heading.text}:\n")
            server_error_value = self.search_element(server.server_error_value)
            file.write(f"{server_error_value.text}\n")

            # succes Rate:
            success_rate_heading = self.search_element(server.success_rate_heading)
            file.write(f"{success_rate_heading.text}:\n")
            success_rate_value = self.search_element(server.sucess_rate_value)
            file.write(f"{success_rate_value.text}\n")

            # Total Logs:
            file.write(f"\n{'*' * 20} Log Monitoring {'*' * 20}\n")
            total_logs_heading = self.search_element(server.Total_logs_heading)
            file.write(f"{total_logs_heading.text}:\n")
            total_logs_value = self.search_element(server.Total_logs_value)
            file.write(f"{total_logs_value.text}\n")

            # Info details:
            info_heading = self.search_element(server.Info_heading)
            file.write(f"{info_heading.text}:\n")
            info_value = self.search_element(server.Info_value)
            file.write(f"{info_value.text}\n")

            # Warning:
            warn_heading = self.search_element(server.Warning_heading)
            file.write(f"{warn_heading.text}:\n")
            warn_value = self.search_element(server.Warning_value)
            file.write(f"{warn_value.text}\n")

            # Error:
            error_heading = self.search_element(server.Error_heading)
            file.write(f"{error_heading.text}:\n")
            error_value = self.search_element(server.Error_value)
            file.write(f"{error_value.text}\n")

            # Debug:
            debug_heading = self.search_element(server.Debug_heading)
            file.write(f"{debug_heading.text}:\n")
            debug_value = self.search_element(server.Debug_value)
            file.write(f"{debug_value.text}\n")

            #Heap Usage:
            file.write(f'{'*'*20} JVM-Metrics {"*"*20}')
            heap_usage_heading=self.search_element(server.Heap_usage_heading)
            file.write(f"{heap_usage_heading.text}:\n")
            head_usage_value=self.search_element(server.Heap_usage_value)
            file.write(f"{head_usage_value.text}\n")

            #GC Frequency:
            gc_freq_heading=self.search_element(server.GC_Frequency_heading)
            file.write(f"{gc_freq_heading.text}:\n")
            gc_freq_value=self.search_element(server.GC_Frequency_value)
            file.write(f"{gc_freq_value.text}\n")

            #Thread Count:
            head_count_heading=self.search_element(server.Thread_count_heading)
            file.write(f"{head_count_heading.text}\n")
            head_count_value=self.search_element(server.Thread_count_value)
            file.write(f"{head_count_value.text}\n")

            #CPU Usage:
            cpu_usage_heading=self.search_element(server.CPU_Usage_heading)
            file.write(f"{cpu_usage_heading.text}\n")
            cpu_usage_value=self.search_element(server.CPU_Usage_value)
            file.write(f"{cpu_usage_value.text}\n")

            #Memory Usage:
            memory_usage_heading=self.search_element(server.Memory_usage_heading)
            file.write(f"{memory_usage_heading.text}:\n")
            memory_usage_value=self.search_element(server.Memory_usage_value)
            file.write(f"{memory_usage_value.text}\n")
