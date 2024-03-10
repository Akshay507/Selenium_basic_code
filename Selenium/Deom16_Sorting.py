import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r'C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserSortedVeggies = []
# Click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedviggieList (A,B,C)
vegggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in vegggieWebElements:
    browserSortedVeggies.append(ele.text)
originalBrowserSortedList = browserSortedVeggies.copy()
# Sort this browserSortedveggieList -> (A,B,C)
sortedList = browserSortedVeggies.sort()
assert browserSortedVeggies == originalBrowserSortedList
time.sleep(4)



