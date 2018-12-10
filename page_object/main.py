#coding=utf-8

import time
import HTMLTestRunnerCN
import unittest
import os
import common

def unittest_run():
    case_path = 'D:\\project_git_wzd\\atx_script\\page_object\\case'
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTests(test_case)

    fp = open('/project_git_wzd/atx_script/page_object/report.html','wb')      #生成测试报告HTMLTestRunnerCN
    runner = HTMLTestRunnerCN.HTMLTestRunner(fp,'csc_report','csc_init')  
    #runner = unittest.TextTestRunner()      #不带报告，直接使用unittest的TextTestRunner方法执行用例
    #runner.run(discover)           
    runner.run(testunit)
    fp.close()

if __name__ == "__main__":
    unittest_run()
    common.del_pyc()