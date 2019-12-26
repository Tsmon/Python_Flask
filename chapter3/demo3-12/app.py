from flask import Flask,render_template

app = Flask(__name__)

'''
    静态文件的加载：包括css js img 等等
'''

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
