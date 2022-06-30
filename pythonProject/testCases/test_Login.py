import time
from testCases.confitest import setup
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_Login(self, setup):
        self.driver = webdriver.Chrome("C:\\Users\\Bestpeers\\Music\\chromedriver.exe")
        # self.driver = webdriver.Chrome(setup)
        self.driver.get(self.baseURL)
        self.logger.info("****Browser Launched****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.driver.save_screenshot(".\\Screenshots\\Login_Creds.png")
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.save_screenshot(".\\Screenshots\\Login_Success.png")
        self.logger.info("****Successfully Logged In****")
        self.driver.close()
