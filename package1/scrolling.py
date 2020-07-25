from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#scroll down to pixel
driver.execute_script("window.scrollBy(0,1500)","")
time.sleep(10)

#scroll down to element
flag=driver.find_element_by_xpath("//td[contains(text(),'India')]")
driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll down to end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

