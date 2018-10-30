#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import optimize_report
import time
import unittest

class csc_init(unittest.TestCase):
    browser = webdriver.Chrome()
    browser.get('https://192.168.219.226/uap/login')
    browser.maximize_window()
    print"this is init!"

    def test_1(self):
        self.browser.find_element_by_id('username').send_keys('admin')
        self.browser.find_element_by_id('password').send_keys('1234567890')
        self.browser.find_element_by_name('submit').click()
        self.browser.find_element_by_link_text('CSC7.5.0-227').click()

    def test_2(self):
        #服务管理菜单-点击
        time.sleep(2)
        try:
            self.browser.find_element_by_link_text('服务管理').click()
        except NoSuchElementException as e:
            optimize_report.get_windows_img(self.browser)
            raise e

    def test_3(self):
        #创建服务按钮-点击
        time.sleep(2)
        try:
            self.browser.find_element_by_css_selector('#xxpage-content > div.page-body > div > div.col-md-9.vmsBox > div.widget > div.widget-body > div.table-toolbar.no-padding-top > div > div > a').click()
            optimize_report.get_windows_img(self.browser)
        except NoSuchElementException as e:
            optimize_report.get_windows_img(self.browser)
            raise e


    def test_4(self):
        #磁盘服务tab-点击
        #time.sleep(2)
        self.browser.find_element_by_css_selector('#page-content > div.page-body > div.row > div.col-md-9.vmsBox > div.widget.margin-bottom-10 > div > div.tabbable.tooltipBox > ul > li:nth-child(2) > a').click()


if __name__ == "__main__":
    unittest.main()