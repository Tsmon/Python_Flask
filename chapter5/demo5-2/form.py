#encoding:utf-8
from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,length

class BaseLogin(Form):
    #用户名
    name = StringField('name',validators=[DataRequired(message="用户名不能为空"),length(6,16,message="长度位于6~16之间")],
                       render_kw={'placeholder':'输入用户名'})
    #密码
    password = PasswordField('password',validators=[DataRequired(message="密码不能为空"),length(6,16,message="长度位于6~16之间")],
                        render_kw={'placeholder':'请输入密码'})
