from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('.\drivers/chromedriver')
driver = webdriver.Chrome(s)
driver.get("http://www.euroexam.com/registration-form")
driver.maximize_window()
driver.close()
