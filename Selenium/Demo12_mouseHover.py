import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = r'C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()         # right click
action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).click().perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(8)