#coding=utf-8
from selenium import webdriver
import sys
sys.path.append("..")
from Add_job import add_job
import time
import unittest
import mysql

class testcase1_addjob(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://job.zuzuche.net/web?admin=1"
        self.jobname_text = "运营专员"
        self.jobdesc_text = "运营专员描述"
        self.jobquire_text = "运营专员要求"

    def test1(self):

        before = mysql.connect()

        case1 = add_job(self.driver,self.url)
        case1.open()
        case1.admin()
        case1.admin_go()
        case1.addjob()
        time.sleep(2)
        case1.type_jobname(self.jobname_text.decode('utf-8'))
        time.sleep(2)
        case1.chose_jobaddress()
        time.sleep(2)
        case1.chose_department()
        time.sleep(2)
        case1.chose_jobaddress()
        time.sleep(2)
        case1.chose_JobLevelstart()
        time.sleep(2) 
        case1.chose_JobLevelend()
        time.sleep(2)
        case1.type_jobdesc(self.jobdesc_text.decode('utf-8'))
        time.sleep(2)
        case1.type_jobrequire(self.jobquire_text.decode('utf-8'))
        time.sleep(2)
        case1.submit()
        time.sleep(2)
        case1.submit_yes()
        time.sleep(2)
        case1.accept_alert(self.driver)#处理页面告警

        after = mysql.connect() #数据库校验

        case1.get_windows_img()
        time.sleep(3)
        print "before is %s,after is %s" % \
        (before,after)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()