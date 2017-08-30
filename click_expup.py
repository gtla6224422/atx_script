#coding=utf8
import os
import run_game
import Global
import run_game
import atx
from atx.ext import report
def click_expup(DEVICE,APPID_WETEST):
	try:
		d = atx.connect(DEVICE)
		d.start_app(APPID_WETEST)
		if Global.getHW(d):
			d.wakeup()
			print d.current_app().package
			print Global.getHW(d)[0],Global.getHW(d)[1]
			d.delay(3)  #游戏启动至登录界面所需时间
			d.click_image(r"image/wetest/%dx%d/wetest_step1.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(3)
			d.click_image(r"image/wetest/%dx%d/wetest_step2.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(3)
			d.click_image(r"image/wetest/%dx%d/wetest_step3_testapp.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(3)
			d.click_image(r"image/wetest/%dx%d/wetest_step4.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(10)
			for a in range(2):
				d.click_image(r"image/wetest/%dx%d/wetest_step5.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(20)
			print "开始游戏"
			#d.click_image(r"image/game/%dx%d/sure.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]), timeout=5.0)
			for b in range(2):    #目前游戏登录界面存在bug，需要点击2次进入按钮
				d.click_image(r"image/game/%dx%d/start_game.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]))  #点击匹配图片的屏幕位置

			d.click_image(r"image/game/%dx%d/offline_sure.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			print "进入游戏界面"
			#——————————START:下面可自行编辑自动化内容————————

			d.delay(3)
			d.swipe(624, 586, 178, 514) #720*1280
			#d.swipe(798,688,202,704) #1080*1920
			d.delay(2)
			d.click_image(r"image/game/%dx%d/role.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(2)
			d.click_image(r"image/game/%dx%d/role_3.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(2)
			d.click_image(r"image/game/%dx%d/levelup.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]), timeout=5.0, safe=True)
			for c in range(8000):
				print c
				d.delay(0.25)
			print "结束自动点击"
			#dump_meminfo(d,appid)
			#——————————E    N   D———————————————
			d.click_image(r"image/wetest/%dx%d/wetest_step6.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]),timeout=5.0,safe=True)
			d.delay(3)
			d.click_image(r"image/wetest/%dx%d/wetest_step7.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]), timeout=5.0, safe=True)
			d.delay(3)
			d.click_image(r"image/wetest/%dx%d/wetest_step8.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1]), timeout=5.0, safe=True)
			d.delay(15)
			if d.exists(r"image/wetest/%dx%d/wetest_step9.%dx%d.png"%(Global.getHW(d)[0],Global.getHW(d)[1],Global.getHW(d)[0],Global.getHW(d)[1])):
				print"上传成功"
				d.delay(3)
				d.stop_app(APPID_WETEST)
			else:
				print"上传失败"
				d.delay(3)
				d.stop_app(APPID_WETEST)
		else:
			print "没有适配当前设备分辨率的目标图片"

	except Exception, e:
		print e

