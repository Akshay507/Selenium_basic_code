import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkBoxes))
for checkBox in checkBoxes:
    if checkBox.get_attribute("value") == "option2":
        checkBox.click()
        assert checkBox.is_selected()                              # it is used to select or not
        break
time.sleep(4)


#for checkBox in checkBoxes:
#    if checkBox == checkBoxes[1]:
#        checkBox.click()
#    else:
#        pass