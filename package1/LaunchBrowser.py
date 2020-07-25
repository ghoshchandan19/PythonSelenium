import time

from selenium import  webdriver
from webdriver_manager.firefox import GeckoDriverManager
from dbconnection import *
from webdriver_manager.chrome import ChromeDriverManager

from package1.dbconnection import getOtp
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("https://qa-investor.hdfcfund.com")
driver.find_element_by_id("userId").send_keys("chandan_ghosh")
driver.find_element_by_name("password").send_keys("Test@12345678")
time.sleep(20)
driver.find_element_by_xpath("//input[@class='loginBtn btn btn-bloc ng-scope']").click()
time.sleep(10)
driver.find_element_by_xpath("//input[@id='otp-input']").send_keys(getOtp())
time.sleep(10)
driver.find_element_by_class_name("loginBtn btn btn-bloc ng-scope").click()


print(driver.title)


