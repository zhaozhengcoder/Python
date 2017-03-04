#-*- coding:utf-8 -*-
import BaseHTTPServer


#RequestHandler 繼承 BaseHTTPRequestHandler ，所以他自身就有一個path的數據成員
class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	#Page="to doing  wakakak "
	Page='''
	<html>
	<body>
	<table>
	<tr>  <td>Header</td>         <td>Value</td>          </tr>
	<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
	<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
	<tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
	<tr>  <td>Command</td>        <td>{command}</td>      </tr>
	<tr>  <td>Path</td>           <td>{path}</td>         </tr>
	</table>
	</body>
	</html>
	'''
	#
	def do_GET(self):
		#self.send_response(200)
		#self.send_header('Content-Type','text/html')
		#self.send_header('Content-Length',str(len(self.Page)))
		#self.end_headers()
		#self.wfile.write(self.Page)
		page=self.create_page()
		self.send_content(page)


	def send_content(self,page):
		self.send_response(200)
		self.send_header('Content-Type','text/html')
		self.send_header('Content-Length','text.html')
		self.end_headers()
		self.wfile.write(page)

	#self.date_time_string 和 client_address[0/1]等等都是父類的書據成員
	def create_page(self):
		values={
			'date_time':self.date_time_string(),
			'client_host':self.client_address[0],
			'client_port':self.client_address[1],
			'command':self.command,
			'path':self.path
		}
		page=self.Page.format(**values)
		return page


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()