from flask import Blueprint
from flask import render_template

"""
蓝图概念:
1、作用让flask项目更加模块化,结构更加清晰,更好的管理项目,达到分层解耦,方便管理
2、使用,一先在蓝图文件中导入Blueprint,二在主app文件中注册蓝图
"""

app_user = Blueprint('user_info', __name__, url_prefix='/UserModule',
                     template_folder="blueprint_templates",
                     static_folder="blueprint_static",
                     subdomain='userinfo')


# 注意
# url_prefix='/UserModule' 后面不需要加斜杠了
# template_folder="blueprint_templates"指定模板查找路径,优先去主路径下template下查找
# user_info 为蓝图名称
# subdomain='userinfo'指定子域名前缀

@app_user.route('/user/')
def user():
    # return "<p>返回用户信息<p>"
    return render_template("user_page.html")
