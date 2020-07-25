from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(
    executable_path=r'C:\Users\Chandan Ghosh\PycharmProjects\SeleniumPython\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get("file:///C:/Users/Chandan%20Ghosh/Desktop/practise.html")
driver.back()
driver.forward()

s1 = Select(driver.find_element_by_name("Country"))
s2=s1.options
print(len(s2))




s1.select_by_index(1)

