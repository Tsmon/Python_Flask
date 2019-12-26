from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    rand1 = random.randint(0,1)     #产生0~1范围内的随机数
    return render_template('index.html',name=rand1)
#当模块被直接运行时，代码将被运行；当模块是被导入时，代码不被执行
if __name__ == '__main__':
    app.run(debug=True)
