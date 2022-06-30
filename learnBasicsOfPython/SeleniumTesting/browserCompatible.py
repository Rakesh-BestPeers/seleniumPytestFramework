from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('./Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.google.com')
