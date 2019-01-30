#coding=utf-8

from BasePage import BasePage
from selenium.webdriver.common.by import By

class add_job(BasePage):

    # 定位器
    switch_loc = (By.ID,'g_iframe')
    username_loc = (By.XPATH, '//input[@data-placeholder="邮箱帐号"]')  #登录账号
    password_loc = (By.XPATH, '//*[@type="password" and @name="password"]')     #登录密码

    admin_loc = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li/a/i')      #点击用户菜单
    admin_go_loc = (By.XPATH,'//*[@id="admin_go"]/a')    #选择进入后台管理

    add_job_loc = (By.XPATH,'//*[@id="job-list"]/div[1]/h1/a/button')     #添加职位按钮
    JobName_loc = (By.ID,'formname')      #职位名称
    department_loc = (By.XPATH,'//*[@id="formname"]')   #部门名称下拉框
    department_v1_loc = (By.XPATH,'//option[@value="46"]') #下拉框value=46 ：海外事业部
    JobAddress2_loc = (By.XPATH,'//*[@id="position-post"]/div[2]/div/label[2]/input') #工作地点-大连
    JobAddress1_loc = (By.XPATH,'//*[@id="position-post"]/div[2]/div/label[1]/span') #工作地点-广州
    JobName_loc = (By.XPATH,'//*[@id="position-post"]/div[2]/div/label[1]/span')
    

    def open(self):
        self._open(self.base_url)

    def implicitly_wait(self,time):
        self.implicitly_wait(time)

    def admin(self):
        self.find_element(*self.admin_loc)
        self.find_element(*self.admin_loc).click()

    def admin_go(self):
        self.find_element(*self.admin_go_loc)
        self.find_element(*self.admin_go_loc).click()     

    def addjob(self):
        self.find_element(*self.add_job_loc).click()

    def chose_jobaddress(self):
        self.find_element(*self.JobAddress2_loc).click()

    def type_jobname(self,jobname):
        self.find_element(*self.JobName_loc).send_keys(jobname)

    def chose_department(self):
        m = self.find_element(*self.department_loc)
        m.find_element(*self.department_v1_loc).click()

