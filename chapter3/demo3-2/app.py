from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    title = 'Python的键值对'
    author = 'Tsmon'
#    return render_template('index.html',var1=title,var2=author)
    return render_template('index.html',**locals())

'''
    在render_template()函数中，如果要给模板传递全部的本地变量，可以使用**locals()方法，
    此时，在模块中可以直接使用{{title}}和{{author}}来直接使用变量
'''


@app.route('/user/<username>')
def user(username):
    #渲染模板并向模板传递参数
    return render_template('user.html',name=username)

#当模块被直接运行时，代码将被运行；当模块被导入时，代码不被执行
if __name__ == '__main__':
    app.run(debug=True)
