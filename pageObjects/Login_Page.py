from selenium.webdriver.common.by import By


class Login_Class:
    click_login_link_xpath = "//a[normalize-space()='Login']"
    text_username_name = "username"
    text_password_name = "password"
    click_login_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def Click_Login_Link(self):
        self.driver.find_element(By.XPATH, self.click_login_link_xpath).click()

    def Enter_Username(self, username):
        self.driver.find_element(By.NAME, self.text_username_name).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.NAME, self.text_password_name).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(By.XPATH, self.click_login_button_xpath).click()







