from flask import Flask,render_template

app = Flask(__name__)

'''
    宏的属性还包括size、placeholder，详情见page47
'''

@app.route('/')
def hello_world():
    return render_template('index.html')
#当模块被直接运行时，代码将被运行，当模块被导入时，代码不被执行
if __name__ == '__main__':
    app.run()
