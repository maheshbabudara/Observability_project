
class user:
    ms_access=('xpath','//*[@ng-reflect-title="MSERVICES"]/div')
    user_mgm=('xpath','//span[text()="User Management"]')
    users_feature=('xpath','//div[text()="Users"]')
    add_user=('xpath','//span[starts-with(text(),"Add User")]')
    first_name=('xpath','//label[contains(text(),"First Name")]/../../following-sibling::div//input[@placeholder="Firstname"]')
    last_name=('xpath','//label[contains(text(),"Last Name")]/../../following-sibling::div//input[@placeholder="Lastname"]')
    username=('xpath','//label[contains(text(),"User Name")]/../../following-sibling::div//input[@placeholder="Username"]')
    password=('xpath','//label[contains(text(),"Password")]/../../following-sibling::div//input[@placeholder="Password"]')
    description=('xpath','//label[contains(text(),"Description")]/../../following-sibling::div//input[@placeholder="Description"]')
    email=('xpath','//label[contains(text(),"Email ID")]/../../following-sibling::div//input[@placeholder="Email"]')
    applications_field=('xpath','//*[@ng-reflect-place-holder="Select Application"]//input')
    applications_listbox=('xpath','//div[@class="cdk-overlay-connected-position-bounding-box"]/div[@class="cdk-overlay-pane"]//div[@class="ant-select-item-option-content"]')
    role_field=('xpath','//*[@ng-reflect-place-holder="Select Role"]//input')
    role_listbox=('xpath','//*[@class="cdk-virtual-scroll-viewport cdk-virtual-scroll-orientation-vertical"]//div[@class="ant-select-item-option-content"]')
    next_btn=('xpath','//span[contains(text(),"Next")]')
    cancel_btn=('xpath','//span[contains(text(),"Cancel")]')
    save_btn=('xpath','//span[contains(text(),"Save")]')
    previous_btn=('xpath','//span[contains(text(),"Previous")]')


class edit_user:
    ms_access=('xpath','//*[@ng-reflect-title="MSERVICES"]/div')
    user_mgm=('xpath','//span[text()="User Management"]')
    users_feature=('xpath','//div[text()="Users"]')
    edit_user=('xpath','//li[@ng-reflect-title="Edit User" and contains(text(),"Edit User")]')
    edit_permission=('xpath','//li[@ng-reflect-title="Edit User" and contains(text(),"Edit Permission")]')
    add_user=('xpath','//span[starts-with(text(),"Add User")]')
    first_name=('xpath','//label[contains(text(),"First Name")]/../../following-sibling::div//input[@placeholder="Firstname"]')
    last_name=('xpath','//label[contains(text(),"Last Name")]/../../following-sibling::div//input[@placeholder="Lastname"]')
    username=('xpath','//label[contains(text(),"User Name")]/../../following-sibling::div//input[@placeholder="Username"]')
    password=('xpath','//label[contains(text(),"Password")]/../../following-sibling::div//input[@placeholder="Password"]')
    description=('xpath','//label[contains(text(),"Description")]/../../following-sibling::div//input[@placeholder="Description"]')
    email=('xpath','//label[contains(text(),"Email ID")]/../../following-sibling::div//input[@placeholder="Email"]')
    applications_field=('xpath','//*[@ng-reflect-place-holder="Select Application"]//input')
    applications_listbox=('xpath','//div[@class="cdk-overlay-connected-position-bounding-box"]/div[@class="cdk-overlay-pane"]//div[@class="ant-select-item-option-content"]')
    role_field=('xpath','//*[@ng-reflect-place-holder="Select Role"]//input')
    role_listbox=('xpath','//*[@class="cdk-virtual-scroll-viewport cdk-virtual-scroll-orientation-vertical"]//div[@class="ant-select-item-option-content"]')
    update_btn=('xpath','//span[contains(text(),"Update")]')

    

