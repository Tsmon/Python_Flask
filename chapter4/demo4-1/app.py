from flask import Flask,url_for

app = Flask(__name__)

'''
    app.route和add_url_rule简介
        
    
    4-3、Python装饰器
    
'''

# endpoint参数：一旦使用，在使用url_for()反转时就不能使用视图函数名了，而要使用定义的url名
# Flask通过endpoint找到viewfunction(视图函数)
@app.route('/',endpoint='index')    #底层其实是使用add_url_rule实现的
def hello_world():
    return 'Hello World!'

# 定义路由、endpoint等
def my_test():
    return "这是测试页！"
app.add_url_rule(rule='/test/',endpoint='test',view_func=my_test)


# 构建了一个虚拟的请求上下文环境，打印输出
with app.test_request_context():
    print(url_for('test'))
    print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
