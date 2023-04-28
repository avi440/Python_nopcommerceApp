import logging
from datetime import time

import pytest
import self as self
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class LaunchApplication:
    def __init__(self,driver):
        self.driver = driver

    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen(logLevel=logging.INFO)


    def LoginApplication(self):
        LogGen.deletScreenshortFiles()
        LogGen.deletHTMScreenshortFiles()
        self.logger.info("********************* launching the application ***********************")
        # self.driver = setupdriver
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        # to refresh the browser
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        self.lp = Login(self.driver)

        self.lp.setuseremail(self.useremail)
        self.lp.setPasswordName(self.password)
        self.lp.clickLogin()

    def logoutApplication(self):
        self.lp.clickLogout()

    def closeApplication(self):
        self.driver.close()

