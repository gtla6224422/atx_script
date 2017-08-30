#coding=utf8
import os
import run_game
import Global
import run_game
import atx
from atx.ext import report
def check_vit(d):
	if d.exists(r"image/game/720x1280/mult_explore/check_vit.720x1280.png"):
		d.delay(1)
		d.click(680, 718)  # X掉派遣
		d.delay(1)
		d.click(418, 46)  # 呼出GM
		d.delay(1)
		d.click(206, 948)  # 加体力
		d.delay(1)
		d.click(424, 1178)  # 发送GM
		d.delay(1)
		d.click(518, 162)  # X掉GM
		d.delay(1)
		print "加满体力"
		return True
	else:
		print "体力足够，无需补给"
		return False

def test(DEVICE):
		d = atx.connect(DEVICE)
		for i in range(150):
			# ————左上————
			d.click(198, 424) #左上
			d.delay(1)
			d.click(522, 738)#派遣
			d.delay(1)
			d.click(604, 860)#派遣子画面
			if check_vit(d) == True:
				d.click(198, 424)  # 左上
				d.delay(1)
				d.click(522, 738)  # 派遣
				d.delay(1)
				d.click(604, 860)  # 派遣子画面
				d.delay(1)
			d.click(526, 776)#加速派遣
			d.delay(1)
			d.click(514, 764)#确定
			d.delay(1)
			#————左下—————
			d.click(176, 726)#左下
			d.delay(1)
			d.click(522, 738)#派遣
			d.delay(1)
			d.click(604, 860)#派遣子画面
			if check_vit(d) == True:
				d.click(176, 726)  # 左下
				d.delay(1)
				d.click(522, 738)  # 派遣
				d.delay(1)
				d.click(604, 860)  # 派遣子画面
				d.delay(1)
			d.click(526, 776)#加速派遣
			d.delay(1)
			d.click(514, 764)#确定
			d.delay(1)
			#————右下—————
			d.click(522, 730)#右下
			d.delay(1)
			d.click(522, 738)#派遣
			d.delay(1)
			d.click(604, 860)#派遣子画面
			if check_vit(d) == True:
				d.click(522, 730)  # 右下
				d.delay(1)
				d.click(522, 738)  # 派遣
				d.delay(1)
				d.click(604, 860)  # 派遣子画面
				d.delay(1)
			d.click(526, 776)#加速派遣
			d.delay(1)
			d.click(514, 764)#确定
			d.delay(1)
			#————右上—————
			d.click(518, 450)#右上
			d.delay(1)
			d.click(522, 738)#派遣
			d.delay(1)
			d.click(604, 860)#派遣子画面
			if check_vit(d) == True:
				d.click(518, 450)  # 右上
				d.delay(1)
				d.click(522, 738)  # 派遣
				d.delay(1)
				d.click(604, 860)  # 派遣子画面
				d.delay(1)
			d.click(526, 776)#加速派遣
			d.delay(1)
			d.click(514, 764)#确定
			d.delay(1)
		print i

test(Global.DEVICE)