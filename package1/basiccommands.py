from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/")
print(driver.title) #returns title of the page

print(driver.current_url)# returns current url opened

driver.find_element_by_id("btn1").click()

driver.close() #close the focused browser

driver.quit() # close all the browsers



