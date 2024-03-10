import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(products)
assert count > 0
for product in products:
    product_name = product.find_element(By.XPATH, "h4").text
    actualList.append(product_name)
    product.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


sum = 0
CheckPrices = driver.find_elements(By.XPATH, "//table//tr/td[5]/p")
for price in CheckPrices:
    sum = sum + int(price.text)

TotalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == TotalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()


WebDriverWait(driver,8).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

time.sleep(2)