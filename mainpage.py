#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from pages import basepage
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#import users

# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class LoginPage(basepage):
      def check_page_loaded(self):
        return True if self.find_element(*LoginPageLocators.LOGO) else False


      def enter_credentials(self):
        self.driver.find_element(*LoginPageLocators.LOGIN).click()
        return basepage(self.driver)


class LoginPageLocators(object):

    USERNAME=(By.ID,'id_username')
    PASSWORD=(By.ID,'id_password')
    SUBMIT = (By.XPATH,'.//*[@id="login-form"]/div[2]/button')
