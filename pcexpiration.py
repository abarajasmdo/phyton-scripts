__author__ = '210046799'

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver
import json
import sys
# Google Chrome
driver = webdriver.Chrome()

driver.get('https://ge.service-now.com/')
driver.set_window_position(0, 0)
driver.set_window_size(0, 0)
# Enter some text!
text_area = driver.find_element_by_id('username')
text_area.send_keys("210046799")
text_area = driver.find_element_by_id('password')
text_area.send_keys("barcelona82FC")
# Submit the form!
submit_button = driver.find_element_by_name('submitFrm')
submit_button.click()

with open("fullatosso.txt") as input_file:
    with open("results.csv", "w", encoding="utf-8") as output_file:
        print('sso,owner,pc type,pc name,exp date,end warranty', file=output_file)
        for line in input_file:
            # https://ge.service-now.com/cmdb_ci_list.do?sysparm_query=123TEXTQUERY321=210073013^install_status=1^u_asset_type=Desktop^ORu_asset_type=Laptop^ORu_asset_type=Workstation
            sso = line.replace("\n", "")
            ci_link = 'https://ge.service-now.com/cmdb_ci_list.do?sysparm_query=123TEXTQUERY321=' + sso + '^install_status=1^u_asset_type=Desktop^ORu_asset_type=Laptop^ORu_asset_type=Workstation'
            driver.get(ci_link)
            pc_lines = driver.find_elements_by_xpath("//*[@class='linked formlink']")
            # print(pc_lines)
            pc_links = []
            for pc_info in pc_lines:
                pc_links.append(pc_info.get_attribute("href"))

            for pc_link in pc_links:
                # print(pc_link)
                driver.get(pc_link)
                pc_type_field = driver.find_element_by_id('sys_original.cmdb_ci_computer.u_asset_type')
                pc_type = pc_type_field.get_attribute('value')
                pc_name_field = driver.find_element_by_id('sys_readonly.cmdb_ci_computer.name')
                pc_name = pc_name_field.get_attribute('value')
                exp_date_field = driver.find_element_by_id('sys_readonly.cmdb_ci_computer.u_expiration_date')
                exp_date = exp_date_field.get_attribute('value')
                end_date_field = driver.find_element_by_id('sys_readonly.cmdb_ci_computer.u_end_of_warranty')
                end_date = end_date_field.get_attribute('value')
                owner_field = driver.find_element_by_id('sys_display.cmdb_ci_computer.u_ci_assigned_to')
                owner = owner_field.get_attribute('value')
                print(sso + ',"' + owner + '",' + pc_type+ ',' + pc_name + ',' + exp_date + ',' + end_date, file=output_file)
                # print(sso + ',"' + owner + '",' + pc_name + ',' + exp_date + ',' + end_date)

# Close the browser!
driver.quit()
