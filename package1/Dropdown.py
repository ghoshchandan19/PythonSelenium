from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

sel=Select(driver.find_element(By.XPATH,"//select[@id='RESULT_RadioButton-9']"))
#sel.select_by_visible_text("Evening")

#sel.select_by_index(3)

sel.select_by_value("Radio-1")

#count number of options in
print("Number og options",len(sel.options))

#print all the option in dropdown
all_options=sel.options
for options in all_options:
    print("Options are:",options.text)