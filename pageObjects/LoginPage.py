import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.driver = driver


    # locators
    textbox_userName_id = "Email"
    textbox_password_id = "Password"
    login_button_xpath = "//div[@class='buttons']/button[@class='button-1 login-button']"
    # logout_xpath = "//li[@class='nav-item']/a[text()='Logout']"
    link_logout_linktext = "Logout"



    def setuseremail(self,userName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_userName_id).clear()
        self.driver.find_element(By.ID, self.textbox_userName_id).send_keys(userName)

        # self.driver.find_element("id",self.textbox_userName_id).clear()
        # self.driver.find_element("id",self.textbox_userName_id).send_keys(userName)

    def setPasswordName(self,Password):
        time.sleep(2)
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(Password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()