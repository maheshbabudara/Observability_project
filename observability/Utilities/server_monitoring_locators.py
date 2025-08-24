
class server:
    server_monitoring_module=('xpath','//h1[contains(text(),"Server Monitoring")]/parent::div[@class="LogoHeading"]')
    servers_dropdown=('xpath','//select[@class="ng-untouched ng-pristine ng-valid"]')

    #server overview elements:
    application_health_heading=("xpath",'//div[@class="ServerOverview"]//p[contains(text(),"Application Health")]')
    application_health_value=('xpath','//div[@class="ServerOverview"]//p[contains(text(),"Application Health")]/../following-sibling::div/h1')
    server_availability_heading=('xpath','//div[@class="ServerOverview"]//p[contains(text(),"Service Availability")]')
    server_availability_value=('xpath','//div[@class="ServerOverview"]//p[contains(text(),"Service Availability")]/../following-sibling::div/h1')
    No_of_restarts_heading=('xpath','//div[@class="ServerOverview"]//p[contains(text(),"Number of Restarts")]')
    No_of_restarts_value=('xpath','//div[@class="ServerOverview"]//p[contains(text(),"Number of Restarts")]/../following-sibling::div/h1')
    No_of_pods_heading=('xpath','//div[@class="ServerOverview"]//p[contains(text(),"Number of Pods")]')
    No_of_pods_value=('xpath','//div[@class="ServerOverview"]//p[contains(text(),"Number of Pods")]/../following-sibling::div/h1')

    #server metrices:
    CPU_heading=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"CPU")]')
    CPU_percentage=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"CPU")]/following-sibling::h2')
    CPU_cores=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"CPU")]/following-sibling::h4')
    Memory_heading=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Memory")]')
    Memory_percentage=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Memory")]/following-sibling::h2')
    Memory_GB=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Memory")]/following-sibling::h4')
    Disk_heading=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Disk")]')
    Disk_percentage=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Disk")]/following-sibling::h2')
    Disk_GB=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Disk")]/following-sibling::h4')
    Network_heading=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Network")]')
    Network_percentage=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Network")]/following-sibling::h2/span')
    Network_ms=('xpath','//div[@class="serverMetrics"]/div[@class="DataOverviewContainer"]//h1[contains(text(),"Network")]/following-sibling::h4')

    #API Metrices:
    Request_vol_heading=('xpath','//H1[contains(text(),"Request Volume")]')
    Req_vol_value=('xpath','//H1[contains(text(),"Request Volume")]/following-sibling::h2')
    Failed_req_heading=('xpath','//H1[contains(text(),"Failed Request")]')
    Failed_req_value=('xpath','//H1[contains(text(),"Failed Request")]/following-sibling::h2')
    client_error_heading=('xpath','//H1[contains(text(),"4xx Errors")]')
    client_error_value=('xpath','//H1[contains(text(),"4xx Errors")]/following-sibling::h2')
    server_error_heading=('xpath','//H1[contains(text(),"5xx Errors")]')
    server_error_value=('xpath','//H1[contains(text(),"5xx Errors")]/following-sibling::h2')
    success_rate_heading=('xpath','//H1[contains(text(),"Success Rate")]')
    sucess_rate_value=('xpath','//H1[contains(text(),"Success Rate")]/following-sibling::h2')

    #Log Monitoring:
    Total_logs_heading=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Total Logs")]')
    Total_logs_value=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Total Logs")]/following-sibling::h2')
    Info_heading=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Info")]')
    Info_value=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Info")]/following-sibling::h2')
    Warning_heading=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Warn")]')
    Warning_value=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Warn")]/following-sibling::h2')
    Error_heading=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Error")]')
    Error_value=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Error")]/following-sibling::h2')
    Debug_heading=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Debug")]')
    Debug_value=('xpath','//h1[contains(text(),"Log Monitoring")]/../following-sibling::div[@class="DataOverviewContainer"]//h1[contains(text(),"Debug")]/following-sibling::h2')

    #JVM Metrices:
    Heap_usage_heading=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"Heap Usage (%)")]')
    Heap_usage_value=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"Heap Usage (%)")]/following-sibling::h2')
    GC_Frequency_heading=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"GC Frequency (Hz)")]')
    GC_Frequency_value=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"GC Frequency (Hz)")]/following-sibling::h2')
    Thread_count_heading=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"Thread Count")]')
    Thread_count_value=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"Thread Count")]/following-sibling::h2')
    CPU_Usage_heading=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"CPU Usage (%)")]')
    CPU_Usage_value=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"CPU Usage (%)")]/following-sibling::h2')
    Memory_usage_heading=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"Memory Usage (GB)")]')
    Memory_usage_value=('xpath','//div[@class="JVMMetrics"]//h1[contains(text(),"Memory Usage (GB)")]/following-sibling::h2')






