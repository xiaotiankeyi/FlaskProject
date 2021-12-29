from datetime import datetime

from flask import Flask
from flask import render_template

"""
jinja2模板之过滤器
在模板中,过滤器相当于一个函数
把当前的参数传入函数中
基本语法{{ postion|abs }},abs是过滤器名称
"""

app = Flask(__name__)

app.config.from_pyfile("config.py", silent=False)


@app.route("/filter/")
def filter():
    context = {
        'signature': None,  # 空字符串,空字典,空列表
        'persons': ['jack', 'tom', 'lucy'],
        'gender': 1,
        'testimonials': '渣女,他妈的,想让我当冤大头',
        'text': '截取长文本截取长文本截取长文本截取长文本截取长文本截取长文本截取长文本',
        'custom': '小狐狸被替换',
        'time': datetime(2021, 11, 13, 20, 13, 12)
    }

    return render_template("filter.html", **context)


# 自定义过滤器实现替换功能
@app.template_filter('customFilter')
def customFilter(value):
    value = value.replace("小狐狸", '*****')
    return value


# 自定义时间过滤器
@app.template_filter("timeFilter")
def timeFilter(time):
    if isinstance(time, datetime):
        now_time = datetime.now()
        time_deffer = (now_time - time).total_seconds()
        if time_deffer < 60:  # 小于一分钟
            return '刚刚'
        elif time_deffer >= 60 and time_deffer < 60 * 60:  # 大于一分钟小于一小时
            minutes = time_deffer / 60
            return '%s分钟前' % int(minutes)
        elif time_deffer >= 60 * 60 and time_deffer < 60 * 60 * 24:  # 大于一小时小于24小时
            hours = time_deffer / (60 * 60)
            return '%s小时前' % int(hours)
        elif time_deffer >= 60 * 60 * 24 and time_deffer < 60 * 60 * 24 * 30:  # 大于24小时小于30天
            days = time_deffer / (60 * 60 * 24)
            return '%s天前' % int(days)
        else:
            # 大于30后天就返回创建时的时间
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time


if __name__ == "__main__":
    app.run()
