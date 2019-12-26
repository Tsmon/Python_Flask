from flask import Flask,render_template
import sys
app = Flask(__name__)

'''
    补充：
        loop.index  当前迭代的索引（从1开始）
        loop.index0 当前迭代的索引（从0开始）
        loop.first  是否是第一次迭代，返回true/false
        loop.last   是否是最后一次迭代，返回true/false
        loop.length 返回序列的长度
'''
@app.route('/')
def hello_world():
    goods = [
        {
            'name': 'goods1'
        },
        {
            'name': 'goods2'
        },
        {
            'name': 'goods3'
        },
        {
            'name': 'goods4'
        }
    ]
    return render_template('index.html',**locals())
#**goods时要注意是字典类型、**local是列表、键值对类型

def do_index_class(index):
    if index % 3 == 0 :
        return 'line'   #每间隔三行输出line
    else:
        return ''
#使用自定义过滤器添加css、注册该过滤器
#该方法第一个参数是函数名、第二个参数是自定义的过滤器名称
app.add_template_filter(do_index_class,'index_class')

if __name__ == '__main__':
    app.run()
