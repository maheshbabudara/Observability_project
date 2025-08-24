from Library.library import Base
from time import sleep
from Utilities.log_mgm import log

class Log_management(Base):
    def log_details(self, server, time_range,levels,source):
        self.zoomout()
        self.click(log.log_mgm)
        self.log_server(log.select_server,server)
        self.log_timerange(log.select_Timerange,time_range)
        self.log_level(log.select_level,levels)
        self.log_source(log.select_source,source)
        sleep(10)
        #Appending Log Detail:
        with open('log_mgm_details.txt','a',encoding="utf-8") as file:
            file.write(f'{'#'*20}Log Management Details{' '}-{server}-{time_range}-{levels}-{source}{'#'*20}\n\n')
            #Info:
            Info_heading=self.search_element(log.Info_heading)
            file.write(f'{Info_heading.text}:\n')
            Info_value = self.search_element(log.Info_value)
            file.write(f"{Info_value.text}\n")

            #warning:
            Warning_heading=self.search_element(log.Warning_heading)
            file.write(f'{Warning_heading.text}:\n')
            Warning_value = self.search_element(log.Warning_value)
            file.write(f'{Warning_value.text}:\n')

            #Error:
            Error_heading=self.search_element(log.Error_heading)
            file.write(f'{Error_heading.text}:\n')
            Error_value = self.search_element(log.Error_value)
            file.write(f'{Error_value.text}:\n')

            #Debug:
            Debug_heading=self.search_element(log.Debug_heading)
            file.write(f'{Debug_heading.text}:\n')
            Debug_value = self.search_element(log.Debug_value)
            file.write(f'{Debug_value.text}:\n')

            #Total Logs:
            TotalLogs_heading=self.search_element(log.TotalLogs_heading)
            file.write(f'{TotalLogs_heading.text}:\n')
            TotalLogs_value = self.search_element(log.TotalLogs_value)
            file.write(f'{TotalLogs_value.text}:\n')

    def logs(self, server, time_range, levels, source):
        self.zoomout()
        self.click(log.log_mgm)
        self.log_server(log.select_server, server)
        self.log_timerange(log.select_Timerange, time_range)
        self.log_level(log.select_level, levels)
        self.log_source(log.select_source, source)
        sleep(10)

        # Appending Logs:
        with open('Logs.txt', 'a', encoding="utf-8") as file:
            file.write(f'{'#' * 20}Logs{' '}-{server}-{time_range}-{levels}-{source}{'#' * 20}\n\n')
            All_Headings = ('xpath', '//table[@class="logs-table"]//span[@class="header-content"]/span[1]')

            headings=self.search_elements(All_Headings)
            time_stamp = self.driver.find_elements('xpath',
                                                   '//table[@class="logs-table"]//tr[@class="log-row"]/td[@class="timestamp-cell"]')
            source = self.driver.find_elements('xpath', '//table[@class="logs-table"]//tr[@class="log-row"]/td[@class="source-cell"]')
            level = self.driver.find_elements('xpath',
                                              '//table[@class="logs-table"]//tr[@class="log-row"]/td//span[contains(@class,"level-indicator")]')
            message = self.driver.find_elements('xpath',
                                                '//table[@class="logs-table"]//tr[@class="log-row"]/td//div/span')
            for index in range(len(time_stamp)):
                file.write(f'Time Stamp\n')
                file.write(time_stamp[index].text)

                file.write(f'Source:\n')
                file.write(source[index].text)

                file.write(f'level:\n')
                file.write(level[index].text)

                file.write(f'Message:\n')
                file.write(message[index].text)








