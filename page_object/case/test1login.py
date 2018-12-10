#coding=utf-8
from selenium import webdriver
#from basepage import BasePage
import sys
sys.path.append("..")
from LoginPage import LoginPage
import common
import time
import unittest

class Test1_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://you.163.com/"
        self.username = "nonop01@163.com"
        self.password = "hg633533"

    def test1(self):
        login_page = LoginPage(self.driver,self.url,u"music.163")
        login_page.open()
        login_page.type_login()
        #login_page.implicitly_wait(30)
        login_page.choose_mail_login()
        time.sleep(1)
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.type_sumbit()
        time.sleep(1)
        login_page.get_windows_img()
        time.sleep(2)

    def tearDown(self):
        common.del_pyc()
        self.driver.close()
