from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()

print(driver.current_window_handle)# prints the current window id


handles=driver.window_handles#returns set of window ids
print(handles)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=='Frames & windows':
        driver.close()






