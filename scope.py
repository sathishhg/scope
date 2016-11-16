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


hh_name= "Fazals1"
hh_location = "mi"
hh_count = "1"
hh_memberDOB = "1986-10-12"

intervention_name = "I - Smart Card"
short_Desc = "Smartcard"
activity = "Cash-Assistance for Flood Victims"
sDate = "2015-10-13"
eDate = "2015-12-20"
members ="1"
weeks = "1"
beneficiary = "Beneficiaries"
defaultBeneficiary = "Beneficiaries"
deliveryMechanism = "SmartCard160905 | WFP Smart Card"
currency = "currency"


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
            'saveChanges1':".//*[@id='main-form']/div[1]/input[1]",

            #Intervention Locators
            'Projects': "//*[@id='office_menu']/li[2]/ul/li/a",
            'Project': "//*[@id='django-tables2']/tbody/tr[1]/td[2]/a",
            'NewIntervention': ".//*[@id='content']/div[2]/a",
            'interVenName': "id_name",
            'shortDesc':"id_short_description",
            'activity': "id_activity",
            'startDate': "id_start_date",
            'endDate': "id_end_date",
            'allowedAltMembers': "id_allowed_delegates",

            'beneficaryGroup': "id_beneficiary_groups",
            'defaultBenficiaryGroup': "id_default_beneficiary_group",
            'weeksPerCycle': "id_weeks_per_cycle",
            'deliveryMechanism': "id_delivery_mechanism",
            'Area': "dynatree-checkbox",
            'partnerRoles': "//*[@id='id_required_partner_roles_add_all_link']",
            'saveIntervention': "//*[@id='main-form']/div[20]/input[1]",
            'saveInterPartners': "//*[@id='main-form']/input[6]",

            #Add FoodBasket Locators
            'FoodBasket': "//*[@id='main-form']/input[6]",







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

    #def register_household(self):
       # driver = self.driver
        driver.find_element_by_id(locators['office']).click()
         driver.find_element_by_xpath(locators['houseHolds']).click()
         time.sleep(5)
         driver.find_element_by_xpath(locators['activeHouseholds']).click()
         time.sleep(5)
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
        
         driver.find_element_by_xpath(locators['saveChanges1']).click()
        
         time.sleep(10)

    def addNewIntervention(self):
        driver = self.driver
        driver.find_element_by_xpath(locators['Projects']).click()
        driver.find_element_by_xpath(locators['Project']).click()
        driver.find_element_by_xpath(locators['NewIntervention']).click()
        driver.find_element_by_id(locators['interVenName']).send_keys(intervention_name)
        driver.find_element_by_id(locators['shortDesc']).clear()
        driver.find_element_by_id(locators['shortDesc']).send_keys(short_Desc)
        Select(driver.find_element_by_id(locators['activity'])).select_by_visible_text(activity)
        driver.find_element_by_id(locators['startDate']).clear()
        driver.find_element_by_id(locators['startDate']).send_keys(sDate)
        #driver.find_element_by_id("id_conditionality")).click()
        driver.find_element_by_id(locators['endDate']).clear()
        driver.find_element_by_id(locators['endDate']).send_keys(eDate)
        driver.find_element_by_id(locators['allowedAltMembers']).clear()
        driver.find_element_by_id(locators['allowedAltMembers']).send_keys(members)

        driver.find_element_by_id(locators['weeksPerCycle']).send_keys(weeks)
        Select(driver.find_element_by_id(locators['beneficaryGroup'])).select_by_visible_text(beneficiary)
        Select(driver.find_element_by_id(locators['defaultBenficiaryGroup'])).select_by_visible_text(defaultBeneficiary)
        Select(driver.find_element_by_id(locators['deliveryMechanism'])).select_by_visible_text(deliveryMechanism)
       # driver.find_element_by_id(locators['currency']).send_keys(currency)
        driver.find_element_by_class_name(locators['Area']).click()
        driver.find_element_by_xpath(locators['partnerRoles']).click()
        driver.find_element_by_xpath(locators['saveIntervention']).click()

        driver.find_element_by_xpath(locators['FoodBasket']).click()
        #driver.find_element_by_css_selector("input.btn.btn-primary").click()
       # driver.find_element_by_css_selector("input.btn.btn-primary").click()
        #driver.find_element_by_css_selector("input.btn.btn-primary").click()
       # driver.findElement(By.linkText("")).click()

            
        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
