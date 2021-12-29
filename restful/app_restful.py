from flask import Flask
from  flask import render_template
from flask import request
from flask_restful import Api
from flask_restful import Resource


app = Flask(__name__)
app.config.from_pyfile("../config.py")

api = Api(app)  # 该方式只适用于在当前文件下写flask-restful接口使用

"""flask基本上使用"""
# 定义视图类
class Login(Resource):
    def get(self):
        return {'name':'jack'}

    def post(self):
        return {'username':'tom'}

# 映射url
api.add_resource(Login, "/login/", endpoint='login')


if __name__ == "__main__":
    app.run()