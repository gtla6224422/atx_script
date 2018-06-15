# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('http://music.163.com/')
    browser.maximize_window()
    #browser.switch_to_frame('g_iframe')
    #browser.find_element_by_xpath('//*[@id="auto-id-bbFJp7rpV6l1UiuZ"]').send_keys('2333')
    browser.find_element_by_class_name('txt').send_keys('2333')
    browser.find_element_by_class_name('txt').send_keys(Keys.ENTER)
    #print (browser.page_source)

login()