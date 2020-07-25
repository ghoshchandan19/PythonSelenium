from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
driver.implicitly_wait(10)
# Count number of input boxes
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))

#To verify the test boxes is displayed
status=driver.find_element_by_id("RESULT_TextField-1").is_displayed()
print("Status of tex box:",status)

status=driver.find_element_by_id("RESULT_TextField-1").is_enabled()
print("Status of text box:",status)

#To input the text find
status=driver.find_element_by_id("RESULT_TextField-1").send_keys("Chandan")





