# -*- coding: utf-8 -*-
import re
import datetime
import os


def runBaidu(x):
	my_file = file(x,"r+")
	cur_date = datetime.date.today()
        yester_date = cur_date - datetime.timedelta(days=1)
        result_file_name = str(yester_date) + "_result" + ".txt"
	#result_file_name = "2016-01-20_result.txt"
	result_path = os.path.join('/home/liao/下载/biomart/logs/', result_file_name)
	count_baiduspider = 0
	count_mobile = 0
	count_infosupply = 0
	count_experiment = 0
	count_news = 0
	count_stdproduct = 0
	count_search = 0
	mobile_ua = "Mozilla/5.0 \(Linux;u;Android 4.2.2;zh-cn;\) AppleWebKit/534.46 \(KHTML,like Gecko\) Version/5.1 Mobile Safari/10600.6.3"
	
	regular = "^GET\w*HTTP$"
	
	for s in my_file.readlines():
		is_baidu = re.findall("Baiduspider",s)
		is_mobile = re.findall(mobile_ua,s)
		is_infosupply = re.findall("/infosupply/",s)
		is_experiment = re.findall("/experiment/",s)
		is_news = re.findall("/news/",s)
		is_std = re.findall("/stdproduct/",s)
		is_search = re.findall("/product/",s)
		if len(is_baidu) > 0:
			count_baiduspider += 1
			if len(is_search) > 0:
				count_search += 1
			if len(is_mobile) > 0:
			#url = re.findall("\/\w*\/\w*",s)
				count_mobile += 1
				if len(is_infosupply) > 0:
					count_infosupply += 1
				elif len(is_experiment) > 0:
					count_experiment += 1
				elif len(is_news) > 0:
					count_news += 1
				elif len(is_std) > 0:
					count_stdproduct += 1
	print "BaiduSpider:%d" %(count_baiduspider)
	print "BaiduMobile:%d" %(count_mobile)
	print "MobileInfosupply:%d" %(count_infosupply)
	print "MobileExperiment:%d" %(count_experiment)
	print "MobileNews:%d" %(count_news)
	print "MobileStd:%d" %(count_stdproduct)
	print "Search_item:%d" %(count_search)

	with open (result_path,"w") as f:
		f.write(str("BaiduSpider:%d\n" %(count_baiduspider)))
		f.write(str("BaiduMobile:%d\n" %(count_mobile)))
		f.write(str("MobileInfosupply:%d\n" %(count_infosupply)))
		f.write(str("MobileExperiment:%d\n" %(count_experiment)))
		f.write(str("MobileNews:%d\n" %(count_news)))
		f.write(str("MobileStd:%d\n" %(count_stdproduct)))
		f.write(str("Search_item:%d\n" %(count_search)))
