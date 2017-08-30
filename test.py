#coding=utf8
import os,re,time
import run_game
import Global
import run_game
import atx
from atx.ext import report
import subprocess
def test(DEVICE):
		d = atx.connect(DEVICE)
		for i in range(30):
			d.delay(1)
			for i in range(2):
				d.click(362, 1224)#切到挂机
			d.delay(20)
			d.click(110, 1230)#主页
			d.delay(1)
			d.click(542, 388)#大苍穹
			d.delay(10)
			d.press.home()
			d.delay(20)
			d.start_app('com.test.app')
			d.delay(10)
			print i

#r = os.popen(r'E:\fzmxw\branches\app_0_5\client_exe\simulator\win32\game.exe')
'''cmd = r'E:\fzmxw\branches\app_0_5\client_exe\simulator\win32\game.exe'
data = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
li = data.stdout.readline()
print li'''

"biao"
"oio"
"ih"
"esss"
"last"
"!!!!"