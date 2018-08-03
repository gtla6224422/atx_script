# coding=utf-8
import time
import HTMLTestRunnerCN
import unittest
import logging

def get_windows_img(driver):
        logger = logging.getLogger(__name__)
        file_path = 'D:/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        print(screen_name)
        try:
            driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            #get_windows_img()

case_path = 'D:\\project_git_wzd\\atx_script\\web_autoscripts\\test_case'
testunit = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(case_path,pattern="select*.py",top_level_dir=None)
for test_suit in discover:
    for test_case in test_suit:
        testunit.addTests(test_case)
        #print testunit

#testunit.addTest(csc_init("login"))

fp = open('/project_git_wzd/atx_script/web_autoscripts/report.html','wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(fp,'csc_report','csc_init')   

runner.run(testunit)    
fp.close()