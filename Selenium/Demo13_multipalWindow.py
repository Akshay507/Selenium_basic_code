import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r'C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "openwindow").click()
window = driver.window_handles[1]
driver.find_element(By.ID, "opentab").click()
tab = driver.window_handles[2]
driver.switch_to.window(window)
driver.find_element(By.LINK_TEXT, "Courses").click()
driver.switch_to.window(tab)
driver.find_element(By.LINK_TEXT, "Contact").click()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("akshay")
time.sleep(3)
