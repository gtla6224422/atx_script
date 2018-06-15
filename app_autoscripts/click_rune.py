#coding=utf8
import os
import run_game
import Global
import run_game
import atx
from atx.ext import report
def click_rune(DEVICE,APPID_WETEST):
	try:
		d = atx.connect(DEVICE)
		d.start_app(APPID_WETEST)
		d.delay(3)  #游戏启动至登录界面所需时间
		d.click_image(r"image/wetest/1080x1920/wetest_step1.1080x1920.png",timeout=5.0,safe=True)
		d.delay(3)
		d.click_image(r"image/wetest/1080x1920/wetest_step2.1080x1920.png",timeout=5.0,safe=True)
		d.delay(3)
		d.click_image(r"image/wetest/1080x1920/wetest_step3_acfun.1080x1920.png",timeout=5.0,safe=True)
		d.delay(3)
		d.click_image(r"image/wetest/1080x1920/wetest_step4.1080x1920.png",timeout=5.0,safe=True)
		d.delay(10)
		for a in range(2):
			d.click_image(r"image/wetest/1080x1920/wetest_step5.1080x1920.png",timeout=5.0,safe=True)
		d.delay(20)
		print "开始游戏"
		d.click_image(r"image/game/1080x1920/sure.1080x1920.png", timeout=5.0, safe=True)
		for b in range(2):    #目前游戏登录界面存在bug，需要点击2次进入按钮
			d.click_image(r"image/game/1080x1920/start_game.1080x1920.png")  #点击匹配图片的屏幕位置

		d.click_image(r"image/game/1080x1920/offline_sure.1080x1920.png",timeout=5.0,safe=True)
		print "进入游戏界面"
		#——————————START:下面可自行编辑自动化内容————————

		d.delay(3)
		#d.swipe(624, 586, 178, 514) #720*1280
		d.swipe(798,688,202,704) #1080*1920
		d.delay(2)
		d.click_image(r"image/game/1080x1920/rune.1080x1920.png",timeout=5.0,safe=True)
		for c in range(1000):
			print c
			d.click(100, 1554)#720*1280(60, 1032)
			d.delay(1.0)
			d.click(294, 1566)#720*1280(192, 1032)
			d.delay(1.0)
			d.click(494, 1552)#720*1280(326, 1032)
			d.delay(1.0)
			d.click(710, 1564)#720*1280(464, 1032)
			d.delay(1.0)
			d.click(958, 1562)#720*1280(618, 1032)
			d.delay(1.0)
		print "结束自动点击"
		#dump_meminfo(d,appid)
		#——————————E    N   D———————————————
		d.click_image(r"image/wetest/1080x1920/wetest_step6.1080x1920.png",timeout=5.0,safe=True)
		d.delay(3)
		d.click_image(r"image/wetest/1080x1920/wetest_step7.1080x1920.png", timeout=5.0, safe=True)
		d.delay(3)
		d.click_image(r"image/wetest/1080x1920/wetest_step8.1080x1920.png", timeout=5.0, safe=True)
		d.delay(15)
		if d.exists(r"image/wetest/1080x1920/wetest_step9.1080x1920.png"):
			print"上传成功"
			d.delay(3)
			d.stop_app(APPID_WETEST)
		else:
			print"上传失败"
			d.delay(3)
			d.stop_app(APPID_WETEST)
	except Exception, e:
		print e


