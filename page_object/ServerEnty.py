#coding=utf-8

from BasePage import BasePage
from selenium.webdriver.common.by import By

class ServerEntry(BasePage):

    # 定位器
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    submit_loc = (By.NAME, 'submit')
    csc_entry_loc = (By.XPATH,'//*[@id="app"]/div[3]/div[2]/div/ul/li[5]')
    server_entry_loc = (By.XPATH,'//*[@id="menuListId"]/li[2]/a/span')
    base_url = 'https://192.168.219.226/uap/login'

    def open(self):
        self._open(self.base_url)

    def set_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def set_password(self,password):
        self.find_element(*self.password_loc).clear
        self.find_element(*self.password_loc).send_keys(password)

    def choose_cscentry(self):
        self.find_element(*self.csc_entry_loc).click()

    def type_sumbit(self):
        self.find_element(*self.submit_loc).click()


