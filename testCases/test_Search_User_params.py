import time

from Utilities.readProperties import ReadconfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.Search_User import Search_user_Class


class Test_Search_User:
    username = ReadconfigFile.Read_username()
    password = ReadconfigFile.Read_password()


    def test_search_user_params_005(self,setup,getDataForSearchUser):
        self.driver = setup
        self.Li = Login_Class(self.driver)
        self.Li.Click_Login_Link()
        self.Li.Enter_Username(self.username)
        self.Li.Enter_Password(self.password)
        self.Li.Click_Login_Button()
        self.Seu = Search_user_Class(self.driver)
        self.Seu.User_Management()

        Search_Username=getDataForSearchUser[0]
        print(Search_Username)
        Expected_result = getDataForSearchUser[1]
        print(Expected_result)

        self.Seu.Username(Search_Username)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.Seu.CLIckSearch_user()
        # time.sleep(4)
        if self.Seu.Validate_search_user() == "pass" and Expected_result=="pass":
            assert True
        elif self.Seu.Validate_search_user() == "pass" and Expected_result == "fail":
            assert False
        elif self.Seu.Validate_search_user() == "fail" and Expected_result == "pass":
            assert False
        elif self.Seu.Validate_search_user() == "fail" and Expected_result == "fail":
            assert True

