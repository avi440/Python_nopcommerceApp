from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    def __init__(self,driver):
        self.driver = driver

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//*[text()=' Customers']"
    btnAddnew_xpath = "//a[@class='btn btn-primary' and  text()]"
    txtEmail_xpath = "//input[@class='form-control text-box single-line' and @type='email']"
    Password_xpath = "//input[@id='password' and @type='password']"
    firstName_xpath = "//input[@id='FirstName' and @type='text']"
    LastName_xpath = "//input[@id='LastName' and @type='text']"
    genderMale_xpath = "//input[@type='radio']//following-sibling::label[@for='Gender_Male']"
    genderFmale_xpath = "//input[@type='radio']//following-sibling::label[@for='Gender_Female']"
    dateofbarth_xpath = "//input[@name='DateOfBirth']"
    companyName_xpath = "//input[@name='Company']"
    IsTaxExemptChechedBox_xpath = "//input[@id='IsTaxExempt']"
    NewsletterClickEmpty_xpath = "//div[@class='input-group-append']//div[@class='k-multiselect-wrap k-floatwrap']"
    newseletterYourstorename_xpath = "//li[@class='k-item' and text()='Your store name']"
    newseletterTeststore2_xpath = "//li[@class='k-item' and text()='Test store 2']"
    CustomerrolesClickEmpty_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover']//div[@role='listbox']"
    CustomerrolesAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    CustomerrolesForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    CustomerrolesGuests_xpath = "//li[contains(text(),'Guests')]"
    CustomerrolesRegistered_xpath = "//li[contains(text(),'Registered')]"
    CustomerrolesVendors_xpath = "//li[contains(text(),'Vendors')]"
    selectManagerofvendor_xpath = "//select[@class='form-control valid']"
    ActiveChechedBox_xpath = "//Input[@class='check-box' and @id='Active']"
    Admincomment_xpath = "//textarea[@class='form-control']"
    saveButton_xpath = "//button[@class='btn btn-primary' and @name='save']"
    addCustomerSuccessfullymassage_xpath = "//div[@class='alert alert-success alert-dismissable' and text()']"

    def clickonLnkCustomers(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickonLnkCustomersmenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()
        # btn = self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()
        # self.driver.execute_script("arguments[0].click();", btn)



    def clickAddnewButton(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmailToCustomer(self,Email):
        self.driver.find_element(By.ID,self.txtEmail_xpath).clear()
        self.driver.find_element(By.ID,self.txtEmail_xpath).send_keys(Email)

    def setPasswordToCustomer(self,Email):
        self.driver.find_element(By.ID,self.Password_xpath).clear()
        self.driver.find_element(By.ID,self.Password_xpath).send_keys(Email)

    def setFirstNameToCustomer(self,firstName):
        self.driver.find_element(By.ID,self.firstName_xpath).clear()
        self.driver.find_element(By.ID,self.firstName_xpath).send_keys(firstName)

    def setLastNameToCustomer(self,LastName):
        self.driver.find_element(By.ID,self.LastName_xpath).clear()
        self.driver.find_element(By.ID,self.LastName_xpath).send_keys(LastName)

    def clickgenderMaleRadioButton(self):
        self.driver.find_element(By.XPATH, self.genderMale_xpath).click()

    def clickgenderfeMaleRadioButton(self):
        self.driver.find_element(By.XPATH, self.genderFmale_xpath).click()

    def setDateofbarth(self,dateofbarth):
        self.driver.find_element(By.ID,self.dateofbarth_xpath).clear()
        self.driver.find_element(By.ID,self.dateofbarth_xpath).send_keys(dateofbarth)

    def setCompanyName(self,companyName):
        self.driver.find_element(By.ID,self.companyName_xpath).clear()
        self.driver.find_element(By.ID,self.companyName_xpath).send_keys(companyName)

    def clickIsTaxExemptChechedBox(self):
        self.driver.find_element(By.XPATH, self.IsTaxExemptChechedBox_xpath).click()

    def clickNewsletterClickEmpty(self):
        self.driver.find_element(By.XPATH, self.NewsletterClickEmpty_xpath).click()

    def clicknewseletterYourstorename(self):
        self.driver.find_element(By.XPATH, self.newseletterYourstorename_xpath).click()

    def clicknewseletterTeststore2(self):
        self.driver.find_element(By.XPATH, self.newseletterTeststore2_xpath).click()

    def clickCustomerrolesClickEmpty(self):
        self.driver.find_element(By.XPATH, self.CustomerrolesClickEmpty_xpath).click()

    def clickCustomerrolesAdministrators(self):
        self.driver.find_element(By.XPATH, self.CustomerrolesAdministrators_xpath).click()

    def clickCustomerrolesForumModerators(self):
        self.driver.find_element(By.XPATH, self.CustomerrolesForumModerators_xpath).click()

    def clickCustomerrolesGuests(self):
        self.driver.find_element(By.XPATH, self.CustomerrolesGuests_xpath).click()

    def selectManagerofvendor(self,value):
        select = Select(self.driver.find_element(By.XPATH, self.selectManagerofvendor_xpath))
        # select by visible text
        select.select_by_visible_text('value')

    def setAdmincomment(self,Admincomment):
        self.driver.find_element(By.ID,self.Admincomment_xpath).clear()
        self.driver.find_element(By.ID,self.Admincomment_xpath).send_keys(Admincomment)

    def clicksaveButtonButton(self):
        self.driver.find_element(By.XPATH, self.saveButton_xpath).click()

    def VerifyAddCustomerSuccessfullymassage(self):
       return self.driver.find_element(By.XPATH, self.addCustomerSuccessfullymassage_xpath).is_displayed()














