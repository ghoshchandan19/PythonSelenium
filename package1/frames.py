from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.selenium.dev/selenium/docs/api/java/")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

time.sleep(5)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Alert").click()
time.sleep(5)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")

driver.find_element_by_xpath("/html/body/div[2]/ul/li[5]").click()

driver.close()
