#coding=utf-8
from selenium import webdriver
#from basepage import BasePage
from LoginPage import LoginPage

import time
import unittest

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://192.168.219.226/uap/login"
        self.username = "admin"
        self.password = "1234567890"

    def test_userlogin(self):
        login_page = LoginPage(self.driver,self.url,u"CSC")
        login_page.open()
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.type_sumbit()
        login_page.get_windows_img()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()