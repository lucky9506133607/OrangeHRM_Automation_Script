from selenium import webdriver

class chromedriver: 
    driver = None
    def Driver():
        chromedriver.driver = webdriver.Chrome()

"""
def Driver():
    global driver_obj 
    global Test1
    global ThirdCommit
    driver_obj = webdriver.Chrome()
    
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before,
                                 screenshot_condition=TakeScreenshotConditionType.Success)
    with DriverStepSettings(driver_obj, step_settings):
        """
        
    #yield driverz  
    #driver_obj.quit()
"""