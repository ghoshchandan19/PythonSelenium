from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

#Clicking on radio button
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)
if status is False:
    driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

#clicking on checkboxes
driver.find_element_by_xpath("//label[contains(text(),'Sunday')]").click()
status=driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)

