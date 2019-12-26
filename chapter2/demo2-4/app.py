#encoding:utf-8
#导入flask、url_for、redirect模块
from flask import Flask,url_for,redirect

app = Flask(__name__)

'''
    页面重定向
        当用户打开某个页面的时候，我们期望页面跳转到指定的页面，让用户完成某种操作或某个动作
'''

@app.route('/')
def index():
    print("首先访问了index()这个视图函数了！")
    urll=url_for('user_login')      #url_for函数以视图函数作为参数返回 /user_login 这个url
    return redirect(urll)

@app.route('/user_login')       #当url反转后，直接按照 /user_login 这个url访问系统，实现了重定向
def user_login():
    return "这是用户登录页面，请您登录，才能访问首页！"

#当模块被直接执行时，代码将被运行；当模块被导入时，代码不被执行
if __name__ == '__main__':
    app.run()
