from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.get("https://www.google.com")

print(driver.title) # Gets title from the page

driver.back() #Move backward in the browser

driver.forward()#Move forward in the browser