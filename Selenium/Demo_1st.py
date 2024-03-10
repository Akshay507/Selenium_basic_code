from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#step1
driver_path = r"C:\Users\akshay.nv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# step2
#service_obj = Service()
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

#step3
#service_obj = Service("C:/Users/akshay.nv/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
