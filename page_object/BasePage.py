#coding=utf-8

import time
import logging
import os

class BasePage():
    '''页面基础类'''

    # 初始化
    def __init__(self, selenium_driver,base_url,pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.timeout = 10

    # 打开不同的子页面
    def _open(self, url):         
        #print("The url is %s" % url)    
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)
        #assert self.driver.current_url == url, 'Did not load on %s' % url

    def open(self):
        self._open(self.base_url)

    def implicitly_wait(self,time):     #隐性等待时间
        self.driver.implicitly_wait(time)

    # 元素定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def hadle(self):
        now_handle = self.driver.current_window_handle  #得到当前窗口句柄

    def switch(self):
        self.driver.switch_to_frame("g_iframe")

    #截图方法
    def get_windows_img(self):
        logger = logging.getLogger(__name__)
        file_path = 'D:/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        print(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
