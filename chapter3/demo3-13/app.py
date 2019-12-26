from flask import Flask,render_template

app = Flask(__name__)

'''
    模板继承
        模板的继承可以理解为：在一个html文档中已经写好了框架，然后要往里面放东西时
        先用{% block blockname %}{% endblock %}放在一个空的块在里面作为基础模块，
        接下来被别的子模块导入的时候，用子模块里相同名称的模块替代
    
'''

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')


if __name__ == '__main__':
    app.run()
