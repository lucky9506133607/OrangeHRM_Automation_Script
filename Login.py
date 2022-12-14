import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from Driver import chromedriver


"""
Test: Login
    Generated by: Lucky Srivastava (ls2170184@gmail.com)
    Generated on 08/01/2022, 16:40:50
"""

Update_Login_test_Data = pd.DataFrame()




def Test_Data(getCSV):
    global Update_Login_test_Data
    if (getCSV == "OrangeHRM-TestCases - Login-TestData.csv"):
        Login_df = pd.read_csv(getCSV)
        Update_Login_test_Data = Login_df
        return Login_df
    else:
        return None
    
def Update_Test_Data(Status, index_val):
    
    if 'status' not in Update_Login_test_Data.columns:
        Update_Login_test_Data["status"] = None
    if Status == "Passed":
        Update_Login_test_Data["status"][index_val] = "Passed"
    else:
        Update_Login_test_Data["status"][index_val] = "Failed"
        
    return Update_Login_test_Data

def test_Login():
    ChromeDriver_obj = chromedriver
    ChromeDriver_obj.Driver()
    print(Test_Data('OrangeHRM-TestCases - Login-TestData.csv'))
    df = Test_Data('OrangeHRM-TestCases - Login-TestData.csv')
    
    """Automate_Login_Page_test_cases."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://opensource-demo.orangehrmlive.com/"
    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    ChromeDriver_obj.driver.get(ApplicationURL)
    
    for i in range(0, len(df)):
        # 2. Click 'txtUsername'
        time.sleep(3)
        txtusername = ChromeDriver_obj.driver.find_element(By.CSS_SELECTOR, "#txtUsername")
        txtusername.click()
    
        # 3. Type '{Username}' in 'txtUsername'
        txtusername = ChromeDriver_obj.driver.find_element(By.CSS_SELECTOR, "#txtUsername")
        if str(df['Username'][i]) != 'nan':
            txtusername.send_keys(str(df['Username'][i]))
        else:
            txtusername.send_keys('')
    
        # 4. Click 'txtPassword'
        txtpassword = ChromeDriver_obj.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input")
        txtpassword.click()
    
        # 5. Type '{Password}' in 'txtPassword'
        txtpassword = ChromeDriver_obj.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input")
        if str(df['Password'][i]) != 'nan':
            txtpassword.send_keys(str(df['Password'][i]))
        else:
            txtpassword.send_keys('')
            
    
        # 6. Click 'Submit'
        submit = ChromeDriver_obj.driver.find_element(By.CSS_SELECTOR, "#btnLogin")
        submit.click()
    
        # 7. Get text from 'Alert message' if it's visible
        try:
            alert_message = ChromeDriver_obj.driver.find_element(By.CSS_SELECTOR, "#spanMessage")
            print(alert_message.text)
            print(Update_Test_Data('Failed', i))
            
            
        except:
            print("Login Successfull")
            print(Update_Test_Data('Passed', i))
            
            
        # 8. Click 'Welcome rakeshShivamShivam' if it's visible
        try:
            welcome_message = ChromeDriver_obj.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/a[2]")
            welcome_message.click()
        except:
            print('Invalid Username')
        time.sleep(5)
        # 9. Click 'Logout' if it's visible 
        try:
            logout = ChromeDriver_obj.driver.find_element(By.XPATH, "//*[@id='welcome-menu']/ul/li[3]/a")
            logout.click()
        except:
            print('Invalid username')
        
        
