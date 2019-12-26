from flask import Flask,render_template

app = Flask(__name__)

'''
    Flask的过滤器
        1、与字符串操作相关的过滤器
        2、对列表进行操作相关的过滤器
        3、对数值进行操作相关的过滤器
'''
@app.route('/')
def hello_world():
    student = {
        "name" : "Tsmon",
        "age" : -18
    }
    return render_template('index.html',**student)


if __name__ == '__main__':
    app.run()
