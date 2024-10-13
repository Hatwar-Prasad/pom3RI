from selenium.webdriver.common.by import By

from pom.pages.BaseClass import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        self.driver=driver
        self.menubtn=(By.CLASS_NAME,"bm-burger-button")
        self.logoutbtn=(By.LINK_TEXT,"Logout")

    def logout(self):

        self.click(self.menubtn)
        self.click(self.logoutbtn)

