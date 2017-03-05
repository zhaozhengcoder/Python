#coding:utf-8
import sys,os,BaseHTTPServer
from datetime import datetime
import subprocess

class case_cgi_file(object):
	'''脚本文件处理'''
	#判斷一下當前的服務器上有沒有這個文件
	def test(self, requesthandler):
		return os.path.isfile(requesthandler.full_path) and \
			requesthandler.full_path.endswith('.py')

	#如果有的話，就去執行
	def act(self, requesthandler):
		##运行脚本文件
		self.run_cgi(requesthandler)

	#去執行這個python腳本，執行之後將結果返回
	def run_cgi(self,requesthandler):
		data = subprocess.check_output(["python", requesthandler.full_path])
		#將執行的結果返回個瀏覽器
		requesthandler.send_content(data)



path='./echo.py'
res=subprocess.check_output(["python",path])
print res