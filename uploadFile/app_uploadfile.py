import os

from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.datastructures import CombinedMultiDict, ImmutableMultiDict  # 实现文本和文件组合验证
from werkzeug.utils import secure_filename
from wtforms import FileField
from wtforms import Form
from wtforms import StringField
from wtforms.validators import InputRequired

app = Flask(__name__, template_folder='./templates')
app.config.from_pyfile("../config.py")

fileAdders = os.path.join(os.path.dirname(__file__), "images")


# print(fileAdders)


@app.route("/upload/", methods=['get', 'post'])
def upload():
    """上传文件函数"""
    if request.method == 'POST':
        fileInfo = request.files.get('img')
        print('显示文件名', fileInfo.filename)

        """优化包装文件名"""
        filename = secure_filename(fileInfo.filename)

        """保存文件"""
        fileInfo.save(os.path.join(fileAdders, filename))
        return "文件上传成功!!!"
    else:
        return render_template("uploadFile.html")


@app.route('/visitImg/<filename>/')
def visitImg(filename):
    """访问图片,添加图片路径参数和文件名"""
    return send_from_directory(fileAdders, filename)


class WtfImg(Form):
    """通过wtforms来验证文件类型"""
    img = FileField(validators=[FileRequired(message="文件不可为空"),
                                FileAllowed(['jpg', 'png'], message='类型错误')])
    desc = StringField(validators=[InputRequired(message='文件描述不可为空')])


@app.route("/verifyUpload/", methods=['get', 'post'])
def verifyUpload():
    """上传文件函数"""
    if request.method == 'POST':
        form = WtfImg(CombinedMultiDict([request.files, request.form]))
        if form.validate():
            # fileInfo = request.files.get('img')
            # """优化包装文件名"""
            # filename = secure_filename(fileInfo.filename)
            # """保存文件"""
            # fileInfo.save(os.path.join(fileAdders, filename))
            return "文件上传成功并验证通过!!!"
        else:
            print(form.errors)
            return f"{form.errors}"
    else:
        return render_template("uploadFile.html")


if __name__ == "__main__":
    app.run()
    pass
