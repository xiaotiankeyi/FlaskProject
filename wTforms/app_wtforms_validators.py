from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form
from wtforms import StringField, PasswordField,IntegerField  # 导入要验证的字段类型
from wtforms.validators import Length, EqualTo, Regexp  # 导入验证器
from wtforms.validators import InputRequired
app = Flask(__name__, template_folder="./templates")
app.config.from_pyfile("../config.py")

"""
validators常用验证器
Length  长度验证
EqualTo     验证当前字段数据是否和另外一个字段相等
email   邮箱验证
InputRequired   验证是否为必填项,非空
NumberRange     验证数值的区间
Regexp  正则表达式
Url     必须时Url格式
Uuid    必须是uuid类型
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
