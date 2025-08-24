class log:
    log_mgm=('xpath','//div[@class="MenuListContainer"]//h1[contains(text(),"Log Management")]')
    select_server=('xpath','//p[contains(text(),"Select Server")]/following-sibling::select')
    select_Timerange=('xpath','//p[contains(text(),"Select Time Range")]/following-sibling::select')
    select_level=('xpath','//p[contains(text(),"Select Level")]/following-sibling::select')
    select_source=('xpath','//p[contains(text(),"Select Source")]/following-sibling::select')
    #details
    Info_heading=('xpath','//div[@class="metrics-container"]//div[@class="metric-item info"]/descendant::span[@class="metric-label"]')
    Info_value=('xpath','//div[@class="metrics-container"]//div[@class="metric-item info"]/descendant::span[@class="metric-count"]')
    Warning_heading=('xpath','//div[@class="metrics-container"]//div[@class="metric-item warning"]/descendant::span[@class="metric-label"]')
    Warning_value=('xpath','//div[@class="metrics-container"]//div[@class="metric-item warning"]/descendant::span[@class="metric-count"]')
    Error_heading=('xpath','//div[@class="metrics-container"]//div[@class="metric-item error"]/descendant::span[@class="metric-label"]')
    Error_value=('xpath','//div[@class="metrics-container"]//div[@class="metric-item error"]/descendant::span[@class="metric-count"]')
    Debug_heading=('xpath','//div[@class="metrics-container"]//div[@class="metric-item debug"]/descendant::span[@class="metric-label"]')
    Debug_value=('xpath','//div[@class="metrics-container"]//div[@class="metric-item debug"]/descendant::span[@class="metric-count"]')
    TotalLogs_heading=('xpath','//div[@class="metrics-container"]//div[@class="metric-item total"]/descendant::span[@class="metric-label"]')
    TotalLogs_value=('xpath','//div[@class="metrics-container"]//div[@class="metric-item total"]/descendant::span[@class="metric-count"]')

