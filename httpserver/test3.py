#coding:utf-8
import sys,os,BaseHTTPServer

class ServerException(Exception):
	pass


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

	def do_GET(self):
		try:
			print 'get'
			full_path=os.getcwd()+self.path
			print full_path
			print os.getcwd()

			if not os.path.exists(full_path):
				raise ServerException("'{ 0 }'  not found ",format(self.path))
			elif os.path.isfile(full_path):
				self.handle_file(full_path)
			else:
				raise ServerException("unkown object '{ 0 }'",format(self.path))

		except Exception as msg:
			self.handle_error(msg)

	def handle_file(self,full_path):
		try:
			with open(full_path,'rb') as reader:
				content=reader.read()
			self.send_content(content)
		except IOError as msg:
			msg="'{0}' cannot be read :{1} ".format(self.path,msg)
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




