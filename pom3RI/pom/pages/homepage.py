from selenium.webdriver.common.by import By

from pom.pages.BaseClass import BasePage


class HomePage(BasePage):
    def __init__(self,driver):

        self.driver =driver
        self.menubtn=(By.CLASS_NAME,"bm-burger-button")
        self.logoutbtn=(By.LINK_TEXT,"Logout")
        self.addCart_sauceBackpack= (By.XPATH,"(//button[text()='ADD TO CART'])[1]")

    def logout(self):

        self.click(self.menubtn)
        self.click(self.logoutbtn)

    def productFlow(self):
        self.click(self.addCart_sauceBackpack)
        

