#coding=utf-8

from BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    # 定位器
    switch_loc = (By.ID,'g_iframe')
    username_loc = (By.XPATH, '//input[@data-placeholder="邮箱帐号"]')
    password_loc = (By.XPATH, '//*[@type="password" and @name="password"]')
    close_ad_loc = (By.XPATH, '//*[@class="w-close j-close-pop"]')      #关闭广告弹窗
    login_entry_loc = (By.XPATH,'//*[@title="网易严选登录" and @class="j-yx-cp-topLogin"]')    #首页登录按钮
    mail_login_loc = (By.XPATH,'//div[text()="邮箱登录" and @class="yx-headTitle2 yx-f-left j-yx-mailLogin"]')     #选择邮箱登录
    submit_loc = (By.XPATH,'//*[@class="u-loginbtn btncolor tabfocus" and text()="登 录" ]')      #提交登录

    def open(self):
        self._open(self.base_url)

    def implicitly_wait(self,time):
        self.implicitly_wait(time)

    def close_ad(self):
        self.find_element(*self.close_ad_loc).click()

    def type_login(self):
        self.find_element(*self.login_entry_loc).click()

    def choose_mail_login(self):
        self.find_element(*self.mail_login_loc).click()

    def set_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def set_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_sumbit(self):
        self.find_element(*self.submit_loc).click()

