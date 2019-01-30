#coding=utf-8
import urllib
import urllib2
import time
import unittest
import pickle

class testcase2_print(unittest.TestCase):

    def setUp(self):
        print("start")
    def test1(self):
        print("3333")
    def tearDown(self):
        print("end")