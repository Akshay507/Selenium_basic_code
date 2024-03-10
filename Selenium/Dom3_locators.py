import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://rahulshettyacademy.com/angularpractice/")
# ID, Xpath, CSSSelector, classname, name, linkText
driver.find_element(By.NAME, 'email').send_keys("akshay@gmail.come")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("Alqh0308")
driver.find_element(By.ID, 'exampleCheck1').click()


# Xpath //tagname[@attribute='value']
# CSS tagname[attribute='value'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Akshay")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


# Static Dropdown
static = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
static.select_by_visible_text("Male")
static.select_by_index(1)
#static.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
a = driver.find_element(By.CLASS_NAME, "alert-success").text
print(a)
assert "Success" in a
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("AkhsayHello")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(10)

