#coding=utf8
import time
import atx
import Global
from atx.ext import report
#from pytesser import *

def run_click(DEVICE,APPID_GAME):                     #自动点击脚本
	try:
		d = atx.connect(DEVICE)
		d.start_app(APPID_GAME)
		d.delay(25)  #游戏启动至登录界面所需时间
		for a in range(2):                                            #目前游戏登录界面存在bug，需要点击2次进入按钮
			d.click_image(r"E:/pytest/mouse/start_game.720x1280.png")  #点击匹配图片的屏幕位置

		d.click_image("offline_sure.720x1280.png",timeout=5.0,safe=True)
		d.delay(3)
		print "开始测试点击脚本"
		for b in range(20):  #不停切换主菜单画面
			d.click_image("role.720x1280.png",timeout=5.0,safe=True)
			d.click_image("play.720x1280.png",timeout=5.0,safe=True)

		dump_meminfo(d,APPID_GAME)

	except Exception, e:
		print e

	d.stop_app(APPID_GAME)

# main 代码开始
#run_click(Global.DEVICE,Global.APPID_GAME)
