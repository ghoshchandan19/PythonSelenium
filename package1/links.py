from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.lenovo.com/")
links=driver.find_element(By.TAG_NAME,"a")

print("Number of links on the page",len(links))
for link in links:
    print(link.text)#Print all the links on the page
    
