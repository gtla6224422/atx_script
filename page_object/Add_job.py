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
    JobName_loc = (By.XPATH,'//*[@id="formname"]')      #职位名称
    department_loc = (By.XPATH,'//*[@id="formname"]')   #部门名称下拉框
    department_v1_loc = (By.XPATH,'//option[@value="56"]') #下拉框value=55 市场运营中心
    JobAddress2_loc = (By.XPATH,'//*[@id="position-post"]/div[2]/div/label[2]/input') #工作地点-大连
    JobAddress1_loc = (By.XPATH,'//*[@id="position-post"]/div[2]/div/label[1]/span') #工作地点-广州
    #JobName_loc = (By.XPATH,'//*[@id="position-post"]/div[2]/div/label[1]/span')
    JobLevel_start_opt = (By.NAME,'level_from') #职级开始下拉框
    JobLevel_start_value = (By.XPATH,'//*[@id="position-post"]/div[4]/div/div[1]/select/option[2]') #职级开始
    JobLevel_end_opt = (By.NAME,'level_to') #职级结束下拉框
    JobLevel_end_value = (By.XPATH,'//*[@id="position-post"]/div[4]/div/div[2]/select/option[3]')   #职级结束
    HR_opt_loc = (By.XPATH,'//*[@id="user-list"]') #发布HR下拉框
    HR_loc = (By.XPATH,'//option[@value="zzc2018180"]') #发布HR-林东楠:zzc2018180
    JobDesc_loc = (By.XPATH,'//*[@id="description"]') #职位描述
    Jobrequire_loc = (By.XPATH,'//*[@id="requirement"]')    #职位要求

    submit_btn = (By.XPATH,'//*[@value="立即提交"]')    #立即提交
    yes_btn = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]') #是否提交-》提交
    no_btn = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[2]') #是否提交-》取消

    

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

    def chose_JobLevelstart(self):
        s = self.find_element(*self.JobLevel_start_opt)
        s.find_element(*self.JobLevel_start_value).click()

    def chose_JobLevelend(self):
        e = self.find_element(*self.JobLevel_end_opt)
        e.find_element(*self.JobLevel_end_value).click()

    def type_jobdesc(self,jobdesc):
        self.find_element(*self.JobDesc_loc).send_keys(jobdesc)

    def type_jobrequire(self,jobrequire):
        self.find_element(*self.Jobrequire_loc).send_keys(jobrequire)

    def submit(self):
        self.find_element(*self.submit_btn).click()

    def submit_yes(self):
        self.find_element(*self.yes_btn).click()

    def accept_alert(self,driver):
        alert=driver.switch_to_alert() #获取页面警告信息
        alert.accept()  #接收页面警告信息
