# coding=utf-8
import time
import HTMLTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

report_path = 'D:\\report.html'
fp = open(report_path,'wb')
runner = HTMLTestRunner.HTMLTestRunner(fp,'csc_report','csc_init')   

class csc_init(unittest.TestCase):
    browser = webdriver.Chrome()
    browser.maximize_window()
    def login(self):
        time.sleep(1)
        try:
            self.browser.get('https://192.168.219.226/uap/login')
            self.browser.maximize_window()
            self.browser.find_element_by_id('username').send_keys('admin')
            self.browser.find_element_by_id('password').send_keys('1234567890')
            self.browser.find_element_by_name('submit').click()
            self.browser.find_element_by_link_text('CSC7.5.0-227').click()  
            self.browser.find_element_by_css_selector('#dragDiv5 > div.panel-body > div.panel-right-link > select > option:nth-child(10)').click()
            #time.sleep(2)
        except Exception as e:
            self.browser.quit()

testunit = unittest.TestSuite()
testunit.addTest(csc_init("login"))
runner.run(testunit)    
fp.close()