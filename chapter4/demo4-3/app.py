from flask import Flask,render_template,request,views

app = Flask(__name__)

'''
    基于方法的类视图：对每个HTTP方法执行不同的函数，映射到对应方法的小写的同名方法上
'''
@app.route('/')
def hello_world():
    return render_template('index.html')

#定义LoginView类
class LoginView(views.MethodView):
    #当用户通过get方法进行访问的时候执行get方法
    def get(self):
        return render_template('index.html')
    #当用户通过post方法访问的时候执行post方法
    def post(self):
        username = request.form.get('username')
        password = request.form.get('pwd')
        if username == 'admin' and password == 'admin':
            return "用户名正确，可以登录！"
        else:
            return "用户名或密码错误，不可以登录！"

#通过add_url_rule添加类视图和URL的映射关系
app.add_url_rule('/login',view_func=LoginView.as_view('loginview'))


if __name__ == '__main__':
    app.run(debug=True)
