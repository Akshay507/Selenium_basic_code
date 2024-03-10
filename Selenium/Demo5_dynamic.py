import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
# print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))  # this line used to validate the condition
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


# Another methode
#country = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li")
#for i in country:
#    if i.text == "India":
#        i.click()
#    else:
#        pass
#time.sleep(10)
