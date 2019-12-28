#encoding:utf-8
from flask import Blueprint
#创建一个Blueprint对象，第一个参数可看作该Blueprint对象的名称
product_list = Blueprint('products',__name__)
#在一个app里，对象名不能与其余的Blueprint对象名重复
#第二个参数__name__用作初始化
@product_list.route("/products")    #将蓝图对象当做'app'那样使用
def product():
    return "这是产品模块！"