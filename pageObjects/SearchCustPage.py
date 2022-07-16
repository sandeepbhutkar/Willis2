from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SearchCustPage:
    Tab_Admin_ID = "menu_admin_viewAdminModule"
    Tab_UserManagement_ID = "menu_admin_UserManagement"
    Tab_Users_ID = "menu_admin_viewSystemUsers"
    txt_Search_ID = "searchSystemUser_userName"
    btn_Search_ID = "searchBtn"
    Txt_Data_Xpath = "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a"

    def __init__(self, driver):
        self.driver = driver


    def Enter_Search(self,SearchValue):
        var1 = self.driver.find_element(By.ID, self.Tab_Admin_ID)
        var2 = self.driver.find_element(By.ID, self.Tab_UserManagement_ID)
        var3 = self.driver.find_element(By.ID, self.Tab_Users_ID )
        action = ActionChains(self.driver)
        action.move_to_element(var1).move_to_element(var2).move_to_element(var3).click().perform()
        self.driver.find_element(By.ID, self.txt_Search_ID).send_keys(SearchValue)

    def Click_Search_Button(self):
        self.driver.find_element(By.ID, self.btn_Search_ID).click()
        var1 = self.driver.find_element(By.XPATH,self.Txt_Data_Xpath).text
        return var1


