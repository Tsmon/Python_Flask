from flask import Flask,render_template

app = Flask(__name__)
'''
    模板中的控制语句之for语句
        Jinja2中for循环内置常量
'''

@app.route('/')
def hello_world():
    goods = [
        {
            'name':'物品1',
            'price':'100'
        },
        {
            'name': '物品2',
            'price': '200'
        },
        {
            'name': '物品3',
            'price': '300'
        }
    ]
    return render_template('shop.html',**locals())


if __name__ == '__main__':
    app.run()
