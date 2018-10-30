#coding=utf8
import uiautomator2

global DEVICE    #安卓硬件设备号，可通过adb device查看获得
global APPID_WETEST    #app名，可通过adb shell pm list packages查看获得
global APPID_GAME
global DEVICE_MI4 #小米4设备号
global HW_list #分辨率列表，后续可继续添加新分辨率
global displayHeight #设备分辨率高度
global displayWidth #设备分辨率宽度
global APPID_GAME_TEST

DEVICE = 'CB5A1TLH5R'  #安卓硬件设备号，可通过adb device查看获得
DEVICE_MI4 = 'd9998f96'
APPID_WETEST = 'com.tencent.wefpmonitor'  #wetest-app名，可通过adb shell pm list packages查看获得
APPID_GAME = 'com.ylbgj.rastar'  #苍之纪元-星辉包名
APPID_GAME_ACFUN = 'com.tiantuo.czjy.acfun'
APPID_GAME_TEST = 'com.test.app'
HW_list = ((720,1280),(1080,1920))#后续需要维护，可填入新的分辨率，宽高顺序要固定！

def getHW(d):                 #获取当前设备分辨率，判断分辨率是否在目前拥有的设备分辨率范围内。
	displayHeight = d.info['displayHeight']
	displayWidth = d.info['displayWidth']
	if (displayWidth,displayHeight) in HW_list:
		#@print "存在分辨率 %d x %d"%(displayHeight,displayWidth)
		return (displayWidth,displayHeight)
	else:
		#print "不存在分辨率"
		return None



def dump_meminfo(d,appid=None):                 #查看app内存
	func = getattr(d,"adb_shell",None)
	if func is None:
		print "android device only,for now"
		return
	#全部内存
	#if not appid:
		#out = func(['dumpsys','meminfo']).splitlines()[-6]
		#print '\n'.join(out)
		#return
	#app内存
	out = func(['dumpsys', 'meminfo',appid])
	for line in out.splitlines():
		print line
		if 'TOTAL' in line:
			break