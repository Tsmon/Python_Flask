from flask import Flask,render_template,views,url_for

app = Flask(__name__)

'''
    Flask类视图
        分为标准类视图和基于调度方法的类视图
        标准类视图的特点：
            必须继承flask.views.View
            必须实现dispatch_request方法，以后请求过来后，都会执行这个方法，这个方法的返回值相当于之前的视图
        函数，也必须返回Response或者子类的对象，或者是字符串、元组
            必须通过app.add_url_rule(rule,endpoint,view_func)来做URL与视图的映射，view_func参数需要使用as_view类方法转换
            如果指定了endpoint,那么在使用url_for反转时就必须使用endpoint指定的那个值；如果没有指定endpoint，那么就可以使
        用as_view(视图名称)中指定的视图名称来作为反转
        注意：
            使用类视图的好处是继承，可以把一些共性的东西放在父类中，其他子类可以继承，但是类视图不能跟函数视图一样，写完
        类视图还需要通过app.add_url_rule(url_rule,view_func)进行注册
'''
class Ads(views.View):
    def __init__(self):
        super().__init__()
        self.context={
            'ads':'这是对联广告！'
        }
#定义Index类，继承自Ads
class Index(Ads):
    def dispatch_request(self):#使用dispatch_request()方法，定义类视图
        return render_template('index.html',**self.context)

class Login(Ads):
    def dispatch_request(self):
        return render_template('login.html',**self.context)

class Register(Ads):
    def dispatch_request(self):
        return render_template('register.html',**self.context)

#添加视图
app.add_url_rule(rule='/',endpoint='index',view_func=Index.as_view('Index'))#类名称.as_view()什么意思？
app.add_url_rule(rule='/login',endpoint='login',view_func=Login.as_view('Login'))
app.add_url_rule(rule='/register',endpoint='register',view_func=Register.as_view('Register'))

if __name__ == '__main__':
    app.run()
