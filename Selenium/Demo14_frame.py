import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r'C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame(driver.find_element(By.ID, "courses-iframe"))
driver.find_element(By.LINK_TEXT, "Job Support").click()
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("akshay")
time.sleep(3)