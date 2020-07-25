from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
time.sleep(5)
#driver.switch_to.alert.accept()# close the alert using accept

alert_text=driver.switch_to.alert.text #Get the text of the alert
print(alert_text)

driver.switch_to.alert.dismiss() # close the alert using dismiss

driver.close()