from flask import Flask,render_template,request

app = Flask(__name__)

'''
    在本工程中，没有对表单进行有效的保护措施，容易被人利用，想想为什么？
'''

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])     #定义路由，指定访问方法
def login():
    if request.method == 'GET':
        return "这是get请求！"
    else:
        return "这是POST请求！"

if __name__ == '__main__':
    app.run(debug=True)
