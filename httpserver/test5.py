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


#RequestHandler 繼承 BaseHTTPRequestHandler ，所以他自身就有一個path的數據成員
class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	Error_Page="""\
	<html>
	<body>
	<h1>Error accessing {path}</h1>
	<p>{msg}</p>
	</body>
	</html>
	"""
	Cases=[case_cgi_file()]

	#這裏的self其實是  RequestHandler對象
	def do_GET(self):
		try:
			self.full_path = os.getcwd() + self.path
			for case in self.Cases:
				if case.test(self):
					case.act(self)
					break
		except Exception as msg:
			self.handle_error(msg)

	def handle_error(self,msg):
		content=self.Error_Page.format(path=self.path,msg=msg)
		self.send_content(content,404)

	def send_content(self,page,status=200):
		#print 'send_content function '
		self.send_response(status)
		self.send_header('Content-Type','text/html')
		self.send_header('Content-Length','text.html')
		self.end_headers()
		self.wfile.write(page)



if __name__ == '__main__':
	serverAddress = ('', 8081)
	server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
	server.serve_forever()

