'''
Created on May 21, 2017

@author: Smita
'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# get the path of ChromeDriverServer
dir = os.path.dirname("D:\Cloudamize\Jars")
chrome_driver_path = "D:\Cloudamize\Jars\chromedriver.exe"
 
# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page
driver.get("https://enterprise-demo.orangehrmlive.com")
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("admin");
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin");
driver.find_element_by_xpath("//input[@id='btnLogin']").click();
user = driver.find_element_by_xpath("//a[@id='welcome']").text;
print(user)
driver.find_element_by_xpath("//a[@id='welcome']").click();
driver.find_element_by_xpath("//a[text()='Logout']").click();
print("Test Passed")
driver.close()