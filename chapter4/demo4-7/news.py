#encoding:utf-8
from flask import Blueprint
new_list = Blueprint('news',__name__)
# 视图函数的名称不能和蓝图对象的名称一样？(即模块名称不能和蓝图名称一致)
@new_list.route("/news")
def new():
    return "这是新闻模块！"