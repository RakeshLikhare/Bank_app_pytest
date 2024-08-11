from selenium.webdriver.common.by import By


class Search_user_Class:
    click_link_User_Management_xpath= "//a[normalize-space()='User Management']"
    text_Username_name="username"
    click_Search_user_xpath="//button[@type='submit']"
    search_user_page_title_Css="div[class='container'] h2"

    def __init__(self,driver):
        self.driver=driver

    def User_Management(self):
        self.driver.find_element(By.XPATH, self.click_link_User_Management_xpath).click()

    def Username(self,username):
        self.driver.find_element(By.NAME,self.text_Username_name).send_keys(username)

    def CLIckSearch_user(self):
        self.driver.find_element(By.XPATH,self.click_Search_user_xpath).click()

    def Validate_search_user(self):
        title=self.driver.find_element(By.CSS_SELECTOR,self.search_user_page_title_Css).text
        if title=="Edit User":
            return "pass"
        else:
            return "fail"



