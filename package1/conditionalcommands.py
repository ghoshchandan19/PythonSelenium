from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://newtours.demoaut.com/")
user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

round_trip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print("Status of round trip status:",round_trip_radio.is_selected())

one_way_trip=driver.find_element_by_css_selector("input[value=oneway]")
print("Status of oneway trip status:",one_way_trip.is_selected())