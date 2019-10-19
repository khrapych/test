from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome( 'C:/webdrivers/chromedriver.exe' )
driver.get( "http://www.onliner.by" )
assert "Onliner" in driver.title
elem = driver.find_element_by_xpath( "//*[@id='fast-search']/form/input[1]" )
elem.send_keys('Iphone')

time.sleep(2)

driver.switch_to.frame(driver.find_element_by_css_selector( ".modal-iframe" ))
Iphone = driver.find_element_by_xpath( '//*[@id="search-page"]/div[2]/ul/li[2]/div/div/div[2]/div/a' ).click()
if driver.find_element_by_css_selector( '.button.button_big.button_orange.offers-description__button' ):
	print( 'mojno' )


time.sleep(5)
driver.close()
