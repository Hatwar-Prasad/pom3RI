from selenium.webdriver.common.by import By

from pom.pages.BaseClass import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.loginBtn = (By.ID, 'login-button')
        self.actualTitle= 'Swag Labs'



    def login(self,username,password):
        self.sendkeys(self.username_field,username)
        self.sendkeys(self.password_field,password)
        self.click(self.loginBtn)

    def assertTitle(self):

        assert self.driver.title.__eq__(self.actualTitle)

