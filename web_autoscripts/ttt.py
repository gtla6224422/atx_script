from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://192.168.208.110:8099/csc/index.html')

browser.find_element_by_id('username').send_keys('admin')
browser.find_element_by_id('password').send_keys('1234567890')
browser.find_element_by_name('submit').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="menuListId"]/li[2]/a').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="page-content"]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div/a').click()
time.sleep(1)
browser.find_element_by_xpath("//span[contains(text(),'截止')]").click()
time.sleep(2)