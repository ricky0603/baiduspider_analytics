# -*- coding: utf-8 -*-
# !/usr/bin/python

import urllib, urllib2, os
import baiduspider
import datetime

#控制日期，每次运行脚本都自动取昨天的日志
cur_date = datetime.date.today()
yester_date = cur_date - datetime.timedelta(days=1)

# 下载两台服务器的日志文件


#file0 = "web_access_" + "2015-12-05"
file0 = "web_access_" + str(yester_date)
file_name = file0 + ".log"
url = os.path.join('http://192.168.200.224:88/dns01/biomart/', file_name)
url2 = os.path.join('http://192.168.200.224:88/dns02/biomart/', file_name)
path = os.path.join('/home/liao/下载/',file_name)
path2 = os.path.join('/home/liao/下载/' ,file0 + '(1).log')

def loading(done,undo,totally):
	try:
			
		percent =  100 * done * undo / totally
		if percent == 100:
			print 'done'

			
	except:
		print "loading part error"

def downLog(path,url):
	try:
		urllib.urlretrieve(url,path,loading)
	except:
		print "Error", path, url

downLog(path,url)
downLog(path2,url2)

#在本地拼合下载的日志文件

new_file_name = file0 + "_2.log"
new_path = os.path.join("/home/liao/下载/", new_file_name)

with open(path, 'r') as f:
	with open(path2, 'r') as d:
		with open (new_path, 'w') as k:
			k.write(f.read())
			k.write(d.read())
			
			
# 用 baiduspider.py 解析日志		
baiduspider.runBaidu(new_path)
