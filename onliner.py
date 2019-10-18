from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome( 'C:/webdrivers/chromedriver.exe' )
driver.get( "http://www.onliner.by" )
assert "Onliner" in driver.title
elem = driver.find_element_by_xpath( "//*[@id='fast-search']/form/input[1]" )
elem.send_keys('Iphone')



time.sleep(5)
driver.close()