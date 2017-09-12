#! /usr/bin/python
import os,time,datetime
time2sleep = 2.5
print time.strftime('%Y%m%d%H%M%S');
logid = int(time.strftime('%Y%m%d%H%M%S'))
f = open(r"%d.txt"%logid, "w+")
while True:
	str = []
	#str = os.popen('top -bi -n 2 -d 0.02').read().split('\n\n')[0].split('\n')
	str.append(os.popen('top -bi -n 2 -d 1 -p 5490').read().split('\n\n')[0].split('\n'))
	str.append(os.popen('top -bi -n 3 -d 1 -p 5490').read().split('\n\n')[1].split('\n'))
	str_cpuinfo =  str[2]
	str_meninfo = str[3]
	str_actinfo = str[6]
	print (str[2])
	print (str[3])
	print (str[6])
	f.write(str_cpuinfo + "\r\n" + str_meninfo + "\r\n" + str_actinfo + "\r\n")
	time.sleep(time2sleep)
f.close()
