from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source_element=driver.find_element_by_id("box4")
target_element=driver.find_element_by_id("box103")
action=ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()
