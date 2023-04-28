import logging
import time

# from datetime import time

import pytest
import self as self
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


@pytest.mark.usefixtures("setupdriver")
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\LoginPage.xlsx"
    logger = LogGen.loggen(logLevel=logging.INFO)



    def test_login_ddt(self):
        LogGen.deletScreenshortFiles()
        LogGen.deletHTMScreenshortFiles()
        self.logger.info("********** verified the test login ddt001 *****************")
        # self.driver = setupdriver
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.lp = Login(self.driver)

        self.row = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excle: ",self.row)

        self.clum = XLUtils.getColumnCount(self.path,'Sheet1')
        print("Number of colum in Excle ",self.clum)
        lst_status = []  # empty list

        for r in range(2,self.row+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.passw = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setuseremail(self.user)
            self.lp.setPasswordName(self.passw)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            ecp_title = "Dashboard / nopCommerce administration"
            if act_title == ecp_title:
                if self.exp == "Pass":
                    self.logger.info("**** passed 01")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed 01")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != ecp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed 01")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** passed 01")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("******* Login DDT passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("******* Login DDT failed")
            self.driver.close()
            assert False

        self.logger.info("************************* end of the login DDT test ************")
        self.logger.info("******************* Test_002_DDT_Login is compleated ************** ")
















