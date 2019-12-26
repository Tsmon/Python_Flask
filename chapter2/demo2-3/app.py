#encoding:utf-8
from flask import Flask,url_for     # 导入Flask和url_for

app = Flask(__name__)       # flask初始化

@app.route('/')     #定义路由
def index():        #定义视图函数
    #url_for函数根据视图函数和参数进行反转，返回对应的url
    urll = (url_for('news',id='10086'))
    return "URL反转内容为：%s" % urll

@app.route('/news/<id>')
def news(id):
    return u'您请求的参数是：%s' % id

# 当模块直接运行时，代码将被运行；当模块被导入时，代码不被执行
if __name__ == '__main__':
    app.run()
