#coding=utf-8
from selenium import webdriver
import sys
sys.path.append("..")
from Add_job import add_job
import time
import unittest
import pickle

class testcase1_addjob(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://job.zuzuche.net/web?admin=1"
        #pickle.dump(self.driver.get_cookies(),open("cookies.pkl","wb"))
        self.jobname_text = "运营专员"

    def test1(self):
        aj = add_job(self.driver,self.url)
        aj.open()
        aj.admin()
        aj.admin_go()
        aj.addjob()
        time.sleep(1)
        aj.type_jobname(self.jobname_text)
        aj.chose_department()
        aj.chose_jobaddress()
        aj.get_windows_img()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()