import os

from flask import Flask
from flask import render_template
from flask import request
from flask import sessionObj
from wtforms import Form
from wtforms import StringField
from wtforms import ValidationError  # 自定义错误
from wtforms.validators import Length

app = Flask(__name__, template_folder='./templates')
app.config.from_pyfile("../config.py")
app.secret_key = os.urandom(24)
from random import randint
from random import choice


@app.route("/")
def index():
    """生成字母加数字的验证码"""
    code = ''
    for i in range(5):
        num = chr(randint(65, 90))
        string = str(randint(0, 9))
        code += choice([num, string])  # choice返回一个随机数
    sessionObj['code'] = code
    return render_template("uploadFile.html")


class RegisterForm(Form):
    """自定义验证器来验证验证码"""
    code = StringField(validators=[Length(min=5, max=5)])

    def validate_code(self, field):
        """命名规则validate+验证字段"""

        print(field.data.lower(), sessionObj.get('code').lower())
        # print(type(field.data), type(sessionObj.get('code')))
        if field.data.lower() != sessionObj.get('code').lower():
            raise ValidationError(message="验证码输入错误")


@app.route("/register/", methods=['post'])
def register():
    name = request.form['username']
    password = request.form['pwd']
    confirmPwd = request.form['confirmPwd']
    email = request.form['email']
    code = request.form['code']
    # print(name, password, confirmPwd, email, code)

    """进行form表单验证"""
    form = RegisterForm(request.form)
    if form.validate():
        return f'{form.validate()}验证通过'
    else:
        # print(form.errors)
        return f'{form.validate()}验证失败,错误是{form.errors}'


if __name__ == "__main__":
    app.run()
