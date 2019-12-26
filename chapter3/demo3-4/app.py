from flask import Flask,render_template
import random
app = Flask(__name__)

'''
    在模板中，尽量少使用多层嵌套的if-else结构，尽量多用if-elif-else结构
'''
@app.route('/')
def hello_world():
    rad1 = random.randint(1,3)
    return render_template('index.html',name = rad1)
#当模块被直接运行时，代码将被执行；当模块被导入时，代码不被执行
if __name__ == '__main__':
    app.run(debug=True)
