# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class csc_init(object):
    browser = webdriver.Chrome()
    browser.maximize_window()

    def is_element_exist(self,xpath):
        x = self.browser.find_element_by_xpath(xpath)
        if len(x) == 0:
            print "找不到元素"
            return False
        elif len(x) == 1:
            return True
        else:
            print "存在%s个元素：%s" %s(len(x),xpath)


    def login(self):
        browser = webdriver.Chrome()
        time.sleep(3)
        browser.get('https://192.168.219.226/uap/login')
        #browser.switch_to_frame('g_iframe')
        browser.find_element_by_id('username').send_keys('admin')
        browser.find_element_by_id('password').send_keys('1234567890')
        browser.find_element_by_name('submit').click()
        browser.implicitly_wait(10)
        browser.find_element_by_link_text('CSC7.5.0-227').click()
        #print (browser.page_source)
        #if self.is_element_exist('//*[@id="menuListId"]/li[4]/a'):
        browser.find_element_by_xpath('//*[@id="menuListId"]/li[4]/a').click()
        xp = browser.find_element_by_xpath('//*[@id="menuListId"]/li[4]/a')
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="menuListId"]/li[4]/ul/li[2]/a/span').click()
        time.sleep(2)
        browser.find_element_by_css_selector('#page-content > div.page-body > div > div > div.row.wrapper > div > a:nth-child(1)')
        return False

csc = csc_init()
csc.login()