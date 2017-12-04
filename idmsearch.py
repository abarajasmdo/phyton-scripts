__author__ = '210046799'

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver
import json
import sys
# Google Chrome
driver = webdriver.Chrome()

driver.get('http://now.corporate.ge.com')
# Enter some text!
text_area = driver.find_element_by_id('username')
text_area.send_keys("210046799")
text_area = driver.find_element_by_id('password')
text_area.send_keys("CAP82america")
# Submit the form!
submit_button = driver.find_element_by_name('submitFrm')
submit_button.click()

with open("ejemplo1.txt") as input_file:
    with open("results.csv", "w", encoding="utf-8") as output_file:
        for line in input_file:
            driver.get('http://now.corporate.ge.com/rest/v0/search?query='+ line)
            jsonResult = driver.find_element_by_tag_name('body').text
            jsonParsed = json.loads(jsonResult)
            results = jsonParsed["results"]
            if(len(results) > 0):
                ssoTitle= jsonParsed["results"][0]["title"]
                ssoTitle = ssoTitle.replace(" (", ",").replace(")", "")
                print(line.replace("\n", "") + "," + ssoTitle, file=output_file)
# Close the browser!
driver.quit()