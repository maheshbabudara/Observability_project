from Library.library import Base
from time import sleep
from Utilities.locators import Dash

class Dashboard(Base):
    def dash_details(self):
        self.click(Dash.dashboard_menu)
        sleep(10)
        with open("Dashboard_details.txt", "a") as f:
            f.write(f"{'#'*100}\n")
            f.write(f"Dashboard Details\n")
            f.write(f"{'-'*50}\n")

            #Total servers:
            f.write(f"{'*'*20} Servers {'*'*20}\n")
            total_servers_heading=self.search_element(Dash.total_servers_heading)
            f.write(f"{total_servers_heading.text}:\n")
            total_servers_value=self.search_element(Dash.total_servers_value)
            f.write(f"{total_servers_value.text}\n")


            #API Calls:
            f.write(f'{'*' * 20} API {'*' * 20}\n')
            api_calls_heading=self.search_element(Dash.API_Calls_heading)
            f.write(f"{api_calls_heading.text}:\n")
            api_calls_value=self.search_element(Dash.API_Calls_value)
            f.write(f"{api_calls_value.text}\n")

            #Total Logs:
            f.write(f"{'*'*20} Logs {'*'*20}\n")
            logs_heading=self.search_element(Dash.Total_Logs_heading)
            f.write(f"{logs_heading.text}:\n")
            logs_value=self.search_element(Dash.Total_Logs_value)
            f.write(f"{logs_value.text}\n")

            #Alerts:
            f.write(f"{'*'*20} Alerts {'*'*20}\n")
            alerts_heading=self.search_element(Dash.Alerts_heading)
            f.write(f"{alerts_heading.text}:\n")
            alerts_value=self.search_element(Dash.Alerts_value)
            f.write(f"{alerts_value.text}\n")



