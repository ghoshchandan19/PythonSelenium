from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.implicitly_wait(10)

admin=driver.find_element_by_id("menu_admin_viewAdminModule")
user_mngmt=driver.find_element_by_id("menu_admin_UserManagement")
users=driver.find_element_by_id("menu_admin_viewSystemUsers")
actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_mngmt).move_to_element(users).click().perform()