from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://youtube.com')
searchbox =  driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Hitech Choudhary')
searchButton = driver.find_element_by_xpath('//*[@id="button"]/yt-icon')

searchButton.click()

