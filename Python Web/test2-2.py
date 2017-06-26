#encoding:utf-8
#刚才的问题是使用了flask，但是问题是对于每个不同的url，去用python生成html
#这样有一个很大的问题，就是一个复杂的网页往往有很多的html，用python生成这样非常的麻烦
#下面使用模板的方式 来做这个

"""
1. 这个模板的套路，有点像mvc的思想，分离前后端
2. 注意html文件需要在当前目录的文件下，创建一个新的文件夹 templates，然后把html文件放到里面
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

#通过request 来访问提交的表单的username和password
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        #通过给后面给参数的方式，传递username，或者是其他的python生成的参数
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()