import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#---Chrome
#driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
#service = Service(driver_path)
#driver = webdriver.Chrome(service=service)
#____Firefox
driver_path = r"C:\Users\akshay.nv\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.maximize_window()             # To maximize the window
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)             # used show title
print(driver.current_url)       # To know the correct URL
driver.get("https://rahulshettyacademy.com/documents-request")
driver.minimize_window()         # used to minimize the window
time.sleep(4)
driver.back()                    # used to go back
driver.refresh()                 # used to refresh the page
driver.forward()
time.sleep(1)   # used to forward the page
driver.close()