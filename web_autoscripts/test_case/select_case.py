#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import unittest

class csc_init(unittest.TestCase):
    browser = webdriver.Chrome()
    browser.get('https://192.168.219.226/uap/login')
    browser.maximize_window()
    print"this is init!"

    def test_login(self):
        browser = self.browser
        browser.find_element_by_id('username').send_keys('admin')
        browser.find_element_by_id('password').send_keys('1234567890')
        browser.find_element_by_name('submit').click()
        browser.find_element_by_link_text('CSC7.5.0-227').click()  

    def test_vm(self):
        browser = self.browser
        browser.find_element_by_css_selector('#menuListId > li:nth-child(4) > a').click()

    def test_soft(self):
        browser = self.browser
        browser.find_element_by_css_selector('xxx').click()

    def tearDown(self):
        browser = self.browser
        browser.quit()

if __name__ == "__main__":
    unittest.main()