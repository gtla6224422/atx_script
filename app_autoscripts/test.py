#coding=utf-8
import os,re,time
import run_game
import Global
import run_game
import atx
from atx.ext import report
#import uiautomator
import subprocess
def test(DEVICE):
		d = atx.connect(DEVICE)
		for i in range(2):
			d.click(378, 682)
			d.type("233")


test(Global.DEVICE)
#r = os.popen(r'E:\fzmxw\branches\app_0_5\client_exe\simulator\win32\game.exe')