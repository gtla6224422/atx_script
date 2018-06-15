#coding=utf8
import os
import time
import Global
import atx
import run_game,click_rune,click_rune_720x1280,click_expup


#d = Global.start(Global.DEVICE,Global.APPID_WETEST)
#print Global.getHW(d)[0]

def mian():
	click_expup.click_expup(Global.DEVICE, Global.APPID_WETEST)

if __name__ == "__main__":
	mian()