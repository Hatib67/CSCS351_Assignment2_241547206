

from selenium import webdriver
from selenium.webdriver.common.by import By





driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")

driver.get("https://www.google.com/")
driver.maximize_window()
print("Website Application Title is: "+ driver.title)
print("Website Application URL is: "+ driver.current_url)
driver.find_element(By.NAME, 'q').send_keys('FC COLLEGE')

