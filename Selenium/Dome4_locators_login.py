import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/client")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("akshu7443@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Alqh@0308")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Alqh@0308")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(5)