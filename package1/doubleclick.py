from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://testautomationpractice.blogspot.com/")
print(driver.title)
driver.maximize_window()

element = driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")
actions=ActionChains(driver)
actions.double_click(element).perform()#To perform double click

actions.context_click(element).perform()# To do right click



