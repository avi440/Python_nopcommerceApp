import logging
import random
import string
import time

# from datetime import time

import pytest
import self as self
from selenium import webdriver

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from testCases.launchApplication import LaunchApplication
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

@pytest.mark.usefixtures("setupdriver")
class Test_AddCustomer:

    logger = LogGen.loggen(logLevel=logging.INFO)

    @pytest.mark.sanity
    def test_login_ddt(self):
        result = ''.join((random.choice(string.ascii_lowercase+string.digits) for x in range(8)))
        self.launchAPP = LaunchApplication(self.driver)
        self.actAddCustomer = AddCustomer(self.driver)
        self.launchAPP.LoginApplication()
        self.actAddCustomer.clickonLnkCustomers()
        self.actAddCustomer.clickonLnkCustomersmenuitem()
        self.actAddCustomer.clickAddnewButton()
        self.logger.info("********** sending Data in to filed was stated  ************")
        # self.actAddCustomer.setEmailToCustomer(result+".gmail.com")
        # self.actAddCustomer.setPasswordToCustomer("1234")
        # self.actAddCustomer.setFirstNameToCustomer("Avi")
        # self.actAddCustomer.setLastNameToCustomer("Band")
        # self.actAddCustomer.clickgenderMaleRadioButton()
        # self.actAddCustomer.setDateofbarth("4/6/2023")
        # self.actAddCustomer.setCompanyName("student")
        # self.actAddCustomer.clickIsTaxExemptChechedBox()
        # self.actAddCustomer.clickNewsletterClickEmpty()
        # self.actAddCustomer.clicknewseletterYourstorename()
        # self.actAddCustomer.clickCustomerrolesClickEmpty()
        # self.actAddCustomer.clickCustomerrolesAdministrators()
        # # self.actAddCustomer.selectManagerofvendor("Vendor 1")
        # self.actAddCustomer.setAdmincomment("It's Google.")
        # self.actAddCustomer.clicksaveButtonButton()
        # flag = self.actAddCustomer.VerifyAddCustomerSuccessfullymassage()
        # print("##################################   "+flag)
        self.logger.info("****************** data is injected Successfuly **************** ")



        self.launchAPP.logoutApplication()
        self.launchAPP.closeApplication()
        # self.driver.close()























