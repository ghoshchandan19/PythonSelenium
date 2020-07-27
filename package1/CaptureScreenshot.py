from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")

driver.save_screenshot("C:\\Users\Chandan Ghosh\Desktop\Screenshot\image.png") #will save the image in any format

driver.get_screenshot_as_file("C:\\Users\Chandan Ghosh\Desktop\Screenshot\image2.jpg")#Will only save the image file in .png format

