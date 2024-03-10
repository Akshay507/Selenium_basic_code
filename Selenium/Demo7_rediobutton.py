import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


#for radiobutton in radiobuttons:
 #   if radiobutton.get_attribute('value') == "radio2":
  #      radiobutton.click()
   #     assert radiobutton.is_selected()
    #    break
time.sleep(4)