from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com")
driver.find_element_by_id("tab-flight-tab-hp").click()
#time.sleep(2)
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("07/22/2020")
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("07/25/2020")

driver.find_element(By.XPATH,"//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']").click()

wait=WebDriverWait(driver,10)#Craeting the object WebdriverWait Class
element=wait.until(EC.element_to_be_clicable(By.XPATH,""))
element.click()

driver.quit()