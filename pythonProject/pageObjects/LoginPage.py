from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username = "user_email"
    textbox_password = "user_password"
    button_login = "user_login"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(by=By.ID, value=self.textbox_username).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(by=By.ID, value=self.textbox_password).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(by=By.ID, value=self.button_login).click()
