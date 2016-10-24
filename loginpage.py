from pages import basepage
#from pages import basepage
from selenium.webdriver.support.expected_conditions
#from selenium.webdriver.support.expected_conditions import expected_conditions as EC
from selenium.webdriver.common.by import By
import os,json
from selenium.webdriver.support.wait import WebDriverWait

cwd =os.getcwd()
os.chdir('..')
json_path ="data"+os.sep+"json_login.json"
L1 = os.path.join(os.getcwd(),"data","json_login.json")
os.chdir(cwd)

class LoginPage(basepage):

    _username_input_id_locator = "inputusername"
    _password_input_id_locator = "inputpassword"
    _login_click_xpath_locator = ""
    usernameText = ""


def __init__(cls,driver):
       super(LoginPage,cls).__init__(driver)


@property
def eusername(cls):
    try:
        WebDriverWait(cls.driver, 10).until((By.ID,cls._username_input_id_locator))
        return cls.driver.find_element_by_id(cls._username_input_id_locator)
    except Exception, err:
        raise type(err)("login username - searched ID - "
                        + cls._username_input_id_locator + err.message)


@property
def password(cls):
    try:
        WebDriverWait(cls.driver, 10).until(cls.presence_of_element_located(
            (By.ID, cls._password_input_id_locator)))
        return cls.driver.find_element_by_id(cls._password_input_id_locator)
    except Exception, err:
        raise type(err)("login password - searched ID - "
                        + cls._password_input_id_locator + err.message)


@property
def login(cls):
    try:
        WebDriverWait(cls.driver, 10).until(cls.presence_of_element_located(
            (By.XPATH, cls._login_click_xpath_locator)))
        return cls.driver.find_element_by_xpath(cls._login_click_xpath_locator)
    except Exception, err:
        raise type(err)("login button - searched XPATH - "
                        + cls._login_click_xpath_locator + err.message)


def loginDashboard(cls):
    with open(L1) as data_file:
        data_text = json.load(data_file)
        for each in data_text:
            cls.usernameText = each["username"]
            passwordText = each["password"]
            # sleep(5)
            cls.email.clear()
            # sleep(5)
            cls.email.send_keys(cls.usernameText)
            # sleep(5)
            cls.password.clear()
            # sleep(5)
            cls.password.send_keys(passwordText)
            # sleep(5)
            cls.login.click()