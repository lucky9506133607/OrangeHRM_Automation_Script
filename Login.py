import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

"""
Test: Login
    Generated by: Lucky Srivastava (ls2170184@gmail.com)
    Generated on 08/01/2022, 16:40:50
"""

def driver():
    global driver 
    global Test1
    global ThirdCommit
    driver = webdriver.Chrome()
    
    """step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before,
                                 screenshot_condition=TakeScreenshotConditionType.Success)
    with DriverStepSettings(driver, step_settings):
        """
        
    """yield driverz  
    driver.quit()"""

def Test_Data(getCSV):
    if (getCSV == "OrangeHRM-TestCases - Login-TestData.csv"):
        Login_df = pd.read_csv(getCSV)
        return Login_df
    else:
        return None
    
def Update_Test_Data(Status, index_val):
    df = Test_Data('OrangeHRM-TestCases - Login-TestData.csv')
    if 'status' not in df.columns:
        df["status"] = None
    if Status == "Passed":
        df["status"][index_val] = "Passed"
    else:
        df["status"][index_val] = "Failed"
        
    return df

def test_Login():
    driver()
    print(Test_Data('OrangeHRM-TestCases - Login-TestData.csv'))
    df = Test_Data('OrangeHRM-TestCases - Login-TestData.csv')
    
    """Automate_Login_Page_test_cases."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://opensource-demo.orangehrmlive.com/"
    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(ApplicationURL)
    
    for i in range(0, len(df)):
        # 2. Click 'txtUsername'
        time.sleep(3)
        txtusername = driver.find_element(By.CSS_SELECTOR, "#txtUsername")
        txtusername.click()
    
        # 3. Type '{Username}' in 'txtUsername'
        txtusername = driver.find_element(By.CSS_SELECTOR, "#txtUsername")
        if str(df['Username'][i]) != 'nan':
            txtusername.send_keys(str(df['Username'][i]))
        else:
            txtusername.send_keys('')
    
        # 4. Click 'txtPassword'
        txtpassword = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input")
        txtpassword.click()
    
        # 5. Type '{Password}' in 'txtPassword'
        txtpassword = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input")
        if str(df['Password'][i]) != 'nan':
            txtpassword.send_keys(str(df['Password'][i]))
        else:
            txtpassword.send_keys('')
            
    
        # 6. Click 'Submit'
        submit = driver.find_element(By.CSS_SELECTOR, "#btnLogin")
        submit.click()
    
        # 7. Get text from 'Alert message' if it's visible
        try:
            alert_message = driver.find_element(By.CSS_SELECTOR, "#spanMessage")
            print(alert_message.text)
            print(Update_Test_Data('Failed', i))
            
            
        except:
            print("Login Successfull")
            print(Update_Test_Data('Passed', i))
            
            
        # 8. Click 'Welcome rakeshShivamShivam' if it's visible
        try:
            welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/a[2]")
            welcome_message.click()
        except:
            print('Invalid Username')
        time.sleep(5)
        # 9. Click 'Logout' if it's visible 
        try:
            logout = driver.find_element(By.XPATH, "//*[@id='welcome-menu']/ul/li[3]/a")
            logout.click()
        except:
            print('Invalid username')
        
        
