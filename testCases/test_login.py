import logging
from datetime import time

import pytest
import self as self
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setupdriver")
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    logger = LogGen.loggen(logLevel=logging.INFO)


    @pytest.mark.regression
    def test_homePageTitle(self):
        LogGen.deletScreenshortFiles()
        LogGen.deletHTMScreenshortFiles()
        self.logger.info("********** homePageTitle vrification *****************")
        # self.driver = setupdriver
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        act_title = self.driver.title


        if act_title == "Your store. Login":
        # if act_title == "Your store":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("********************* test_login verification ***********************")
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
        act_title = self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
        # if act_title == "Dashboard / administration":
            self.lp.clickLogout()
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False


