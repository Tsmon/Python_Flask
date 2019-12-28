from flask import Flask
import news,produt
app = Flask(__name__)

'''
    Flask蓝图
        蓝图的目的是实现各个模块的视图函数写在不同的py文件中。在主视图中导入分路由视图的模块，并且注册蓝图对象
'''
@app.route('/')
def hello_world():
    return 'Hello World!'

app.register_blueprint(news.new_list)

app.register_blueprint(produt.product_list)

if __name__ == '__main__':
    app.run()
