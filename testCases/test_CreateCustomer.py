from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustPage import SearchCustPage
from utilities import XL_Utilities
import time
import pytest
# pytest -v -s --html=./Reports/report.html testCases/test_CreateCustomer.py
# parallel run - pytest -v -s -n=3 --html=./Reports/report.html testCases/test_CreateCustomer.py


class Test_CreateCustomer:
    URL = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    path = "./testData/TestData.xlsx"
    row = XL_Utilities.GetRowCount(path, "Sheet1")

    def test_CreateCustomer(self):
        for r in range(2, self.row+1):
            self.driver = webdriver.Chrome(executable_path="C:/Users/sbhutkar/Downloads/chromedriver.exe")
            self.driver.get(self.URL)
            self.driver.maximize_window()
            # Login Page
            self.lp = LoginPage(self.driver)
            self.lp.Enter_UserName(self.username)
            self.lp.Enter_Password(self.password)
            self.lp.ClickLoginButton()
            # Search form Excel and Get Value and store in Excel
            self.sp = SearchCustPage(self.driver)
            self.sp.Enter_Search(XL_Utilities.ReadData(self.path, "Sheet1", r, 2))
            #self.sp.Click_Search_Button()
            XL_Utilities.WriteData(self.path, "Sheet1", r, 3, self.sp.Click_Search_Button())
            self.driver.close()
    #pytest -v -s -m smoke --html=./Reports/report.html testCases/test_CreateCustomer.py
    @pytest.mark.smoke
    def test_VerifyLoginTitle(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/sbhutkar/Downloads/chromedriver.exe")
        self.driver.get(self.URL)
        self.driver.maximize_window()
        get_title = self.driver.title
        if get_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/TitleFails.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_VerifyLogin(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/sbhutkar/Downloads/chromedriver.exe")
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.Enter_UserName("sss")
        self.lp.Enter_Password("ppp")
        self.lp.ClickLoginButton()
        current_url= self.driver.current_url
        if current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/LoginFail.png")
            self.driver.close()
            assert False









