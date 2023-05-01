from selenium.webdriver.common.by import By


class BaseUI:
    def __init__(self,driver):
        self.driver = driver

    def element(self,LocatorType,Locator):
        if(LocatorType == "css selector" or LocatorType == "cs"):
            return self.driver.find_element(By.CSS_SELECTOR, Locator)
        elif(LocatorType == "class name" or LocatorType == "cn"):
            return self.driver.find_element(By.CLASS_NAME, Locator)
        elif (LocatorType == "tag name" or LocatorType == "tn"):
            return self.driver.find_element(By.TAG_NAME, Locator)
        elif (LocatorType == "name" or LocatorType == "n"):
            return self.driver.find_element(By.NAME, Locator)
        elif (LocatorType == "partial link text" or LocatorType == "plt"):
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, Locator)
        elif (LocatorType == "link text" or LocatorType == "lt"):
            return self.driver.find_element(By.LINK_TEXT, Locator)
        elif (LocatorType == "xpath" or LocatorType == "x"):
            return self.driver.find_element(By.XPATH, Locator)
        else:
            return self.driver.find_element(By.ID, Locator)

    def sendKeysAction(self,delement,data):
        delement.clear()
        delement.send_keys(data)

    def clickAction(self,delement):
        delement.click()
