from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form
from wtforms import StringField, PasswordField  # 导入要验证的字段类型
from wtforms.validators import Length, EqualTo, Regexp  # 导入验证器

app = Flask(__name__, template_folder="./templates")
app.config.from_pyfile("../config.py")

"""
作用一,做表单验证(服务器端验证,js表单验证为客户端验证)
作用二,做模板渲染(了解)
flask-wtf概念：
底层是借助WTforms来实现的,额外功能,文件上传,CSRF保护
WTForms做表单验证的基本使用
"""


@app.route("/")
def index():
    return render_template("uploadFile.html")


class registerForm(Form):
    """
    定义一个表单注册类
    设置好验证项,和前端页面中的name属性值一致
    """
    username = StringField(validators=[Length(min=2, max=15, message='用户名长度为2至15个字符')])  # 定义好用户名输入框的验证信息
    pwd = PasswordField(validators=[Regexp(regex='[0-9a-zA-Z]\w{6,12}$',
                                                  message='只能包含字母、数字和下划线，长度在6-12之间')])
    confirmPwd = PasswordField(validators=[EqualTo(fieldname='pwd', message='两次密码不一致')])   # EqualTo让其和上面的密码字段保持一致

    pass



@app.route("/register/", methods=['post'])
def register():
    name = request.form['username']
    password = request.form['pwd']
    confirmPwd = request.form['confirmPwd']
    email = request.form['email']
    print(name, password, confirmPwd, email)

    """进行form表单验证"""
    form = registerForm(request.form)
    if form.validate():
        return f'{form.validate()}验证通过'
    else:
        print(form.errors)
        return f'{form.validate()}验证失败,错误是{form.errors}'


if __name__ == "__main__":
    app.run()
