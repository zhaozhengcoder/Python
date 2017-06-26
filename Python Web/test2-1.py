#encoding:utf-8
#使用web框架 flask
#为什么要使用web框架
"""
1. 如果不使用web框架，那么就的使用python+wsgi 这样的方式去写代码
2. 这样也就意味着要对不用的url，不同的method 写很多的判断逻辑去处理
3. 使用web框架，可以有效的减少这样的逻辑代码，提高效率
4. 不同的web框架的设计出发点，哲学，理念都不太一样，所以也有很大的差别
5. 常用的web框架 django，Tornado，flask
"""

from flask import Flask
from flask import request

app = Flask(__name__)

#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样
#这个表示 访问 http://localhost:port/  的时候，调用这个函数，methods表示的是使用的方法，get或是post方法
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

#这个表示 访问 http://localhost:port/signin  的时候调用这个函数,方法是get
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

#这个表示 访问 http://localhost:port/signin  的时候调用这个函数,方法是post
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()