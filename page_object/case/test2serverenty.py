#coding=utf-8
from selenium import webdriver
#from basepage import BasePage
import sys
sys.path.append("..")
from LoginPage import LoginPage
import time
import unittest
import common

class Test2_Server(unittest.TestCase):

    def setUp(self):
        print("1")

    def test2(self):
        print("2222222222")

    def tearDown(self):
        common.del_pyc()
        print("3333333333")
