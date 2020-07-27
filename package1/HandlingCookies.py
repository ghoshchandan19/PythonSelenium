from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")

#Capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies
print(cookies)

#Adding all the cookies to the browser
cookie={'name':'Mycookies','value':'122355'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies
print(cookies)

#Delete the cookie
driver.delete_cookie('Mycookies')
cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies
print(cookies)

#Delete all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies
print(cookies)

