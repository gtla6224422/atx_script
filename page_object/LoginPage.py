#coding=utf-8

from BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    # 定位器
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    submit_loc = (By.NAME, 'submit')

    def open(self):
        self._open(self.base_url)

    def set_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def set_password(self,password):
        self.find_element(*self.password_loc).clear
        self.find_element(*self.password_loc).send_keys(password)

    def type_sumbit(self):
        self.find_element(*self.submit_loc).click()
