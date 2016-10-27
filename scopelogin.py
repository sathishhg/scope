import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_scope(self):
        driver = self.driver
        driver.get("https://test.scope.wfp.org")
       # self.assertIn("Home", driver.title)
        username = driver.find_element_by_id("id_username")
        username.send_keys("sathisha-admin")
        password=driver.find_element_by_id("id_password")
        password.send_keys("sathisha")
        loginbutton=driver.find_element_by_xpath(".//*[@id='login-form']/div[2]/button")
        loginbutton.click()
        #self.assertTrue(driver.find_element_by_link_text("Logout"),"Logout link")


        driver.find_element_by_id("mw-co").click()

        # Register Household to SCOPE online

        driver.find_element_by_xpath(".//*[@id='office_menu']/li[1]/ul/li[1]/span/span").click()
        driver.find_element_by_link_text("Active Households").click()
        self.driver.implicitly_wait(5)
        driver.find_element_by_xpath(".//*[@id='lnk_register_new_household']").click()

        # Enter the details for the Household

        driver.find_element_by_xpath(".//*[@id='id_household-name']").send_keys("Farooqs")

        driver.find_element_by_xpath(".//*[@id='main-form']/div[3]/div/span[1]/span[1]/span").click()

        driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("mi")

        driver.find_element_by_xpath("//li[contains(text(),'Benjamin')]").click()

        driver.find_element_by_xpath(".//*[@id='id_household-claimed_member_count']").send_keys("1")

        driver.find_element_by_xpath(".//*[@id='id_last_name']").send_keys("Benja")

        driver.find_element_by_xpath(".//*[@id='id_date_of_birth_is_exact_0']").click()

        driver.find_element_by_id("id_date_of_birth").send_keys("1988-10-12")
        driver.implicitly_wait(8)
        driver.find_element_by_id("id_date_of_birth").send_keys(Keys.TAB)
        driver.implicitly_wait(10)

        driver.find_element_by_xpath(".//*[@id='id_save_houshold']").click()

        time.sleep(5)

        driver.find_element_by_xpath(".//*[@id='main-form']/div[1]/input[1]").click()
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

