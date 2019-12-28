from flask import Flask,flash
from flask import url_for,render_template
from flask_wtf.csrf import CSRFProtect
#导入定义的BaseLogin
from form import BaseLogin
import config
app = Flask(__name__)

app.config.from_object(config)
'''
    使用Flask-WTF处理表单    
'''

@app.route('/login',methods=('POST','GET'))
def baselogin():
    form = BaseLogin()
    if form.validate_on_submit():
        flash(form.name.data+'|'+form.password.data)
        return '表单数据提交成功'
    else:
        return render_template('login.html',form=form)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
