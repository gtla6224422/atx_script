#coding=utf-8
import os,re,time
import uiautomator2
import time
import subprocess

class log:
	def logid(self):
		logid = int(time.strftime('%Y%m%d%H%M%S'))
		f = open(r"%d.txt"%logid, "w+")

class android:
	def init(self):
		self.d = uiautomator2.connect('CB5A1TLH5R')

	def open_app(self):
		self.d.click(0.113, 0.506)

	def music_list(self):
		time.sleep(1)
		self.d(resourceId = 'com.netease.cloudmusic:id/a8b').click()

	def pop(self):
		time.sleep(1)
		self.d(resourceId = 'com.netease.cloudmusic:id/abr').click()


if __name__ == '__main__':
	android_click = android()
	android_click.init()
	android_click.open_app()
	android_click.music_list()
	android_click.pop()
#r = os.popen(r'E:\fzmxw\branches\app_0_5\client_exe\simulator\win32\game.exe')