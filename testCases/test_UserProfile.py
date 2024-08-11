import time

from selenium.webdriver.common.by import By

from Utilities.Logger import Log_Class
from Utilities.readProperties import ReadconfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.SignUp_Page import SignUp_Class


class Test_UserProfile:
    username = ReadconfigFile.Read_username()
    password = ReadconfigFile.Read_password()
    Log=Log_Class.Log_generator()

    def test_BankApp_Url_001(self, setup):
        """self.Log.debug("this is debug")
        self.Log.info("this is info")
        self.Log.warning("this is info")
        self.Log.error("this is error")
        self.Log.critical("this is critical")"""
        self.Log.info("testcase  test_BankApp_Url_001 is started")
        self.driver = setup
        self.Log.info("opening browser")
        self.Log.info("verifying title ")
        if self.driver.title == "Bank Application":
            self.Log.info("testcase  test_BankApp_Url_001 is passed")
            self.Log.info("taking screenshot ")
            self.driver.save_screenshot(".\\Screenshots\\test_BankApp_Url_001.pass(1).png")
            assert True
        else:
            self.Log.info("testcase  test_BankApp_Url_001 is faile")
            self.Log.info("taking screenshot ")
            self.driver.save_screenshot(".\\Screenshots\\test_BankApp_Url_001(1).fail.png")
            assert False
        self.Log.info("testcase  test_BankApp_Url_001 is completed\n")

    def test_Signup_002(self, setup):
        self.Log.info("testcase test_Signup_002 is started")
        self.driver = setup
        self.Log.info("opening browser")
        self.su = SignUp_Class(self.driver)
        self.su.Click_Signup()
        self.Log.info("Entering the username")
        self.Log.info(generate_random_username())  ##random username generate kar rhe hai isse
        self.su.Enter_Username(generate_random_username())
        self.Log.info("Entering the password")
        self.su.Enter_Password("Mahesh@123")
        self.Log.info("Entering the email")
        self.Log.info(generate_random_email())   ##random email generate kar rhe hai isse
        self.su.Enter_Email(generate_random_email())
        self.Log.info("Entering the phone")
        self.Log.info(generate_random_phone_number())    ##random phone generate kar rhe hai isse
        self.su.Enter_Phone(generate_random_phone_number())
        self.Log.info("click on create user button")
        self.su.Click_CreateUser_Button()
        time.sleep(5)
        self.Log.info("checking user creation")
        if self.su.Validate_User_Creation() == "User created successfully":
            self.Log.info("testcase test_Signup_002 is passed ")
            self.Log.info("taking screenshot ")
            self.driver.save_screenshot(".\\Screenshots\\test_Signup_002(2).pass.png")
            self.Log.info("testcase test_Signup_002 is completed\n")
            assert True
        else:
            self.Log.info("testcase test_Signup_002 is failed ")
            self.Log.info("taking screenshot ")
            self.driver.save_screenshot(".\\Screenshots\\test_Signup_002(2).pass.png")
            self.Log.info("testcase test_Signup_002 is completed\n")
            assert False

    def test_Login_003(self, setup):
        self.Log.info("testcase test_Login_003 is started")
        self.driver = setup
        self.Log.info("opening browser")
        self.Li = Login_Class(self.driver)
        self.Log.info("click on login link ")
        self.Li.Click_Login_Link()
        self.Log.info("Entering username")
        self.Li.Enter_Username(self.username)
        self.Log.info("Entering username")
        self.Li.Enter_Password(self.password)
        self.Log.info("click on login button ")
        self.Li.Click_Login_Button()
        time.sleep(5)
        self.Log.info("checking the page title ")
        if self.driver.title == "Dashboard":
            self.Log.info("testcase test_Login_003 is passed")
            self.Log.info("taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_003(3.1).pass.png")
            self.Log.info("testcase test_Login_003 is complete\n")
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, " //a[normalize-space()='User Management']").click()
            # time.sleep(2)
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   ##page scroll ka liye java script
            # self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()   ##view all user ke sid wala Create user button ka abs xpath hai
            # time.sleep(2)
            assert True
        else:
            self.Log.info("testcase test_Login_003 is failed")
            self.Log.info("taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_003.(3.2).fail.png")
            self.Log.info("testcase test_Login_003 is complete\n")
            assert False

##pageobjects banaya random username and email and phone generate karne ke liye jisse singup wala 002 testcase fail na ho
import random
import string
import time

def generate_random_username(length=6):
    return 'User' + ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_email(domain="gmail.com"):
    return generate_random_username() + "@" + domain

def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k=10))

# Allure report image attach
# Full page screenshot
# Allure decorators
# Random username, email, phone number for signup write python program for this and give the data to signup testcase
