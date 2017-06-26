#encoding:utf-8
from wsgiref.simple_server import make_server

def page_index():
    html='<h1>page index</h1>'
    return [html.encode('utf-8')]

def page_login():
    html='<h1>page login</h1>'
    return [html.encode('utf-8')]

def page_default():
    html='<h1>page default</h1>'
    return [html.encode('utf-8')]
    
def application(environ,start_response):
    #print (environ)
    start_response('200 OK',[('Content-type','text/html')])
    #environ是一个map，environ['PATH_INFO']输出的是 /index.py, 而environ['PATH_INFO'][1:]输出的是 index.py,少掉了 /
    body = '<h1>Hello, %s !</h1>' % (environ['PATH_INFO'][1:] or 'web')

    
    if(environ['PATH_INFO']=='/'):
        return page_index()
    if(environ['PATH_INFO']=='/login'):
        return page_login()
    else:
        return page_default()
    return [body.encode('utf-8')]

httpd=make_server('',8100,application)
print ('serving http on port 8100 ... ')
httpd.serve_forever()
