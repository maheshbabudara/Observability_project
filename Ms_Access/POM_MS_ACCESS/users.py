from time import sleep
from Ms_Access.Library.library import Base
from Ms_Access.Utilities.user_locators import user,edit_user

class users(Base):
    def creation(self,first_name,last_name, username, password, description, email,
                 application,role):
        """ Creation of Users"""
        self.zoom()
        self.click(user.user_mgm)
        self.click(user.users_feature)
        self.click(user.add_user)
        self.send_data(user.first_name, first_name)
        self.send_data(user.last_name, last_name)
        self.send_data(user.username, username)
        self.send_data(user.password, password)
        self.send_data(user.description, description)
        self.send_data(user.email, email)
        self.click(user.applications_field)
        sleep(1)
        self.select_applications(user.applications_listbox, application)
        sleep(1)
        self.click(user.role_field)
        sleep(1)
        self.select_roles(user.role_listbox, role)
        sleep(1)
        self.click(user.next_btn)
        sleep(1)
        self.click(user.save_btn)
        sleep(3)

    def duplicate(self,first_name,last_name, username, password, description, email,
                 application,role):
        """ Creation of Users"""
        self.zoom()
        self.click(user.user_mgm)
        self.click(user.users_feature)
        self.click(user.add_user)
        self.send_data(user.first_name, first_name)
        self.send_data(user.last_name, last_name)
        self.send_data(user.username, username)
        self.send_data(user.password, password)
        self.send_data(user.description, description)
        self.send_data(user.email, email)
        self.click(user.applications_field)
        sleep(1)
        self.select_applications(user.applications_listbox, application)
        sleep(1)
        self.click(user.role_field)
        sleep(1)
        self.select_roles(user.role_listbox, role)
        sleep(1)
        self.click(user.next_btn)
        sleep(1)
        self.click(user.save_btn)
        sleep(3)

    def edit(self,username,new_first_name,new_last_name, new_username, new_description, new_email,
                 new_application,new_role):
        """ Edit of Users"""
        self.zoom()
        self.click(edit_user.user_mgm)
        self.click(edit_user.users_feature)
        # self.click(user.add_user)
        more_option=('xpath',f'//tr[@class="ant-table-row ng-star-inserted"]/td[text()="{username}"]/following-sibling::td/span[@nztype="more"]')
        self.click(more_option)
        self.click(edit_user.edit_user)
        sleep(2)
        self.clear(edit_user.first_name)
        self.send_data(edit_user.first_name, new_first_name)
        self.clear(edit_user.last_name)
        self.send_data(edit_user.last_name, new_last_name)
        self.clear(edit_user.username)
        self.send_data(edit_user.username, new_username)
        self.clear(edit_user.description)
        self.send_data(edit_user.description, new_description)
        self.clear(edit_user.email)
        self.send_data(edit_user.email, new_email)
        self.click(edit_user.applications_field)
        sleep(1)
        self.select_applications(edit_user.applications_listbox, new_application)
        sleep(3)
        self.dynamic_click(edit_user.role_field)
        sleep(2)
        self.select_roles(edit_user.role_listbox, new_role)
        sleep(3)
        self.dynamic_click(edit_user.update_btn)
        sleep(3)

    def edit_permissions(self,username):
        """ Edit of Users"""
        self.zoom()
        self.click(edit_user.user_mgm)
        self.click(edit_user.users_feature)
        # self.click(user.add_user)
        more_option=('xpath',f'//tr[@class="ant-table-row ng-star-inserted"]/td[text()="{username}"]/following-sibling::td/span[@nztype="more"]')
        self.click(more_option)
        self.click(edit_user.edit_permission)
        sleep(2)
        check_box=('xpath','//div[@class="ant-table-content"]//input')
        checkboxes=self.driver.find_elements(*check_box)
        for index in range(2, len(checkboxes)):
            checkbox_locator = ('xpath', f"(//span[@class='ant-checkbox ant-checkbox-checked'])[{index}]")
            self.scroll(checkbox_locator)
            self.click(checkbox_locator)

        self.scroll(edit_user.update_btn)
        sleep(1)
        self.dynamic_click(edit_user.update_btn)
        sleep(3)









