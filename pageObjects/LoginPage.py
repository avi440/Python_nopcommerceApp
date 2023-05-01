import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.BaseUI import BaseUI


class Login(BaseUI):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # locators
    textbox_userName_id = "Email"
    textbox_password_id = "Password"
    login_button_xpath = "//div[@class='buttons']/button[@class='button-1 login-button']"
    # logout_xpath = "//li[@class='nav-item']/a[text()='Logout']"
    link_logout_linktext = "Logout"



    def setuseremail(self,userName):
        time.sleep(2)
        self.sendKeysAction(self.element("id", self.textbox_userName_id), userName)


    def setPasswordName(self,Password):
        time.sleep(2)
        self.sendKeysAction(self.element("id", self.textbox_password_id),Password)


    def clickLogin(self):
        self.clickAction(self.element("xpath", self.login_button_xpath))


    def clickLogout(self):
        self.clickAction(self.element("lt", self.link_logout_linktext))
