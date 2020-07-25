from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://newtours.demoaut.com/")
print(driver.title)

driver.implicitly_wait(10) #seconds

assert "Welcome: Mercury Tours" in driver.title

user_ele=driver.find_element_by_name("userName")
user_ele.send_keys("mercury")

pass_ele=driver.find_element_by_name("password")
pass_ele.send_keys("mercury")

driver.find_element_by_name("login").click()