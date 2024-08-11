import time

from Utilities.readProperties import ReadconfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.Search_User import Search_user_Class


class Test_Search_User:
    username = ReadconfigFile.Read_username()
    password = ReadconfigFile.Read_password()

    def test_search_user_004(self,setup):
        self.driver = setup
        self.Li = Login_Class(self.driver)
        self.Li.Click_Login_Link()
        self.Li.Enter_Username(self.username)
        self.Li.Enter_Password(self.password)
        self.Li.Click_Login_Button()
        self.Seu = Search_user_Class(self.driver)
        self.Seu.User_Management()
        self.Seu.Username("Tushar")  ##Tushar1 dalenge to fail ho jayenga kyoki esa koi user hain he nhi
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  ##--browser firefox karte hai tb ye dena hai kyoki firefox me usko search user wala button nhi dikhta hain isliye scroll karne ke liye vo java script use ki gyi hai baki isme nhi dena hai
        time.sleep(5)
        self.Seu.CLIckSearch_user()
        if self.Seu.Validate_search_user() == "pass":
            assert True
        else:
            assert False




