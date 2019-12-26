#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)
'''
    Jinja2模板引擎
    
'''

@app.route('/')
def index():
    #使用render_template方法渲染模板
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user.html')

#当模块直接被运行时，代码将被运行；当模块是被导入时，代码不被执行
if __name__ == '__main__':
    app.run(debug=True)
