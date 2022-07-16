from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    txt_username_id = "txtUsername"
    txt_password_id = "txtPassword"
    btn_Login_id = "btnLogin"

    def __init__(self, driver):
        self.driver = driver

    def Enter_UserName(self,UserName):
        self.driver.find_element(By.ID, self.txt_username_id).clear()
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(UserName)

    def Enter_Password(self,Password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(Password)

    def ClickLoginButton(self):
        self.driver.find_element(By.ID, self.btn_Login_id ).click()