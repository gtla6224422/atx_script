#coding=utf8

import urllib2

hrsys = urllib2.urlopen("http://112.74.161.79/admin/job/list_page").read()

with open("d:\\new.txt","w+") as f:
    f.write(hrsys)