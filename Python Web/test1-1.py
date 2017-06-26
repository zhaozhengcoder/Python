#encoding:utf-8
from wsgiref.simple_server import make_server

def application(environ,start_response):
    #print (environ)
    start_response('200 OK',[('Content-type','text/html')])
    #environ是一个map，environ['PATH_INFO']输出的是 /index.py, 而environ['PATH_INFO'][1:]输出的是 index.py,少掉了 /
    body = '<h1>Hello, %s !</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

httpd=make_server('',8100,application)
print ('serving http on port 8100 ... ')

httpd.serve_forever()