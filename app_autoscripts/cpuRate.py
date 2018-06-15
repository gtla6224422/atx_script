#! /usr/bin/python
import os,time,datetime,sys
time2sleep = 1
print time.strftime('%Y%m%d%H%M%S');
logid = int(time.strftime('%Y%m%d%H%M%S'))
f = open(r"%d.txt"%logid, "w+")
while True:
	str = []
	str.append(os.popen('top -p 28288').read().split('\n\n')[0].split('\n'))
	str_cpuinfo =  str[2]
	str_meninfo = str[3]
	print (str[2])
	f.write(str_cpuinfo + "\r\n" + str_meninfo + "\r\n" + str_actinfo + "\r\n")
	time.sleep(time2sleep)
f.close()
