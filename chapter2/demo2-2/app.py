#encoding:utf-8     #指定编码
from flask import Flask     #导入Flask模块
app = Flask(__name__)       #Flask实例化

@app.route('/')     #定义路由
def hello_world():  #定义视图函数
    return '这是url传参演示！'

#定义路由，传递的参数名是name，因此需要在函数的形参中定义同名的参数
@app.route('/user/<name>')  #注意，参数需要放在尖括号内；传递参数的语法：'/<参数名>/'
def display_name(name):
    return "接收到的名称为：%s" % name

@app.route('/news/<int:id>')
def list_news(id):
    return "接受到的id为%s" % id
#当模块被直接运行时，代码将被运行；当模块被导入时，代码不被执行
if __name__ == '__main__':
   app.run(debug=True)      #开启调试模式
