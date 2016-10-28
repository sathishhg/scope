#ScriptName : Login.py
#---------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service
import unittest
import os,json,time

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

cwd=os.getcwd()
os.chdir('..')
json_path="data"+os.sep+"json_login.json"
L1 = os.path.join(os.getcwd(),"data","json_login.json")
os.chdir(cwd)

# Input data for Login with url

baseurl = "https://test.scope.wfp.org/login/?next=/"
s_username = "sathisha-admin"
s_password = "sathisha"

# Input data for New Household registration

hh_name= "Farroqs"
hh_location = "mi"
hh_count ="1"
hh_memberDOB = "1986-10-12"


locators = {
            #login locatore
            'usernameTxtBox' : "//*[@id='id_username']",
            'passwordTxtBox' : "//*[@id='id_password']",
            'submitButton' :   "//*[@id='login-form']/div[2]/button",

            # Office selection
            'office': "mw-co",
            'houseHolds': "//*[@id='office_menu']/li[1]/ul/li[1]/span/span",
            'activeHouseholds': "//*[@id='office_menu']/li[1]/ul/li[1]/ul/li[1]/a",
            'registerNewHousehold':"//*[@id='lnk_register_new_household']",
            'addNewHousehold': "//*[@id='lnk_register_new_household']",
            'newHouseholdName':"//*[@id='id_household-name']",
            'location1':"//*[@id='main-form']/div[3]/div/span[1]/span[1]/span",
            'location2':"html/body/span/span/span[1]/input",
            'location3':"//li[contains(text(),'Benjamin')]",
            'hhCount': "//*[@id='id_household-claimed_member_count']",
            'exact_DOB': ".//*[@id='id_date_of_birth_is_exact_0']",
            'hhMemberDOB': "id_date_of_birth",
            'saveChanges': "//*[@id='id_save_houshold']",
            'saveChanges1':"//*[@id='main-form']/div[1]/input[1]"
        }





class scopeLogin(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")

    def test_scope_login(self):
        driver = self.driver
        driver.get(baseurl)
        driver.maximize_window()
    #Clear Username TextBox if already allowed "Remember Me"
        driver.find_element_by_xpath(locators['usernameTxtBox']).clear()
    #Write Username in Username TextBox
        driver.find_element_by_xpath(locators['usernameTxtBox']).send_keys(s_username)
    #Clear Password TextBox if already allowed "Remember Me"
        driver.find_element_by_xpath(locators['passwordTxtBox']).clear()
    #Write Password in password TextBox
        driver.find_element_by_xpath(locators['passwordTxtBox']).send_keys(s_password)
    #Click Login button
        driver.find_element_by_xpath(locators['submitButton']).click()

        driver.find_element_by_id(locators['office']).click()
        driver.find_element_by_xpath(locators['houseHolds']).click()
        driver.find_element_by_xpath(locators['activeHouseholds']).click()
        driver.find_element_by_xpath(locators['addNewHousehold']).click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(locators['newHouseholdName']).send_keys(hh_name)
        driver.find_element_by_xpath(locators['location1']).click()

        driver.find_element_by_xpath(locators['location2']).send_keys(hh_location)

        driver.find_element_by_xpath(locators['location3']).click()
        driver.find_element_by_xpath(locators['hhCount']).send_keys(hh_count)

        #driver.find_element_by_xpath(".//*[@id='id_last_name']").send_keys("Benja")

        driver.find_element_by_xpath(locators['exact_DOB']).click()

        driver.find_element_by_id(locators['hhMemberDOB']).send_keys(hh_memberDOB)
        driver.implicitly_wait(8)
        driver.find_element_by_id("id_date_of_birth").send_keys(Keys.TAB)
        driver.implicitly_wait(10)

        driver.find_element_by_xpath(locators['saveChanges']).click()

        time.sleep(5)

        driver.find_element_by_xpath(locators['saveChanges1']).click()

            def create_intervention(self):
        driver = self.driver
        driver.findElement(By.id("id_name")).sendKeys("TestNewWallets");
        driver.findElement(By.id("id_short_description")).clear();
        driver.findElement(By.id("id_short_description")).sendKeys("TEst");
        driver.findElement(By.id("id_short_description")).clear();
        driver.findElement(By.id("id_short_description")).sendKeys("Test");
        new Select(driver.findElement(By.id("id_activity"))).selectByVisibleText("Cash-Assistance for Flood Victims");
        driver.findElement(By.id("id_end_date")).clear();
        driver.findElement(By.id("id_end_date")).sendKeys("201-05-12");
        driver.findElement(By.id("id_conditionality")).click();
        driver.findElement(By.id("id_end_date")).clear();
        driver.findElement(By.id("id_end_date")).sendKeys("2015-05-20");
        driver.findElement(By.id("id_allowed_delegates")).clear();
        driver.findElement(By.id("id_allowed_delegates")).sendKeys("1");

        
        new Select(driver.findElement(By.id("id_default_beneficiary_group"))).selectByVisibleText("Beneficiaries");
        new Select(driver.findElement(By.id("id_delivery_mechanism"))).selectByVisibleText(
            "TestDeliveryMechanism | Bank account");
        
        driver.findElement(By.cssSelector("input.btn.btn-primary")).click();
        driver.findElement(By.cssSelector("input.btn.btn-primary")).click();
        driver.findElement(By.cssSelector("input.btn.btn-primary")).click();
        driver.findElement(By.linkText("Add new intervention")).click();

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
