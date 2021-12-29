from flask import Flask
from flask import Response
from flask import jsonify

"""
返回响应response,可返回三种类型
1、response 对象及其子对象
2、字符创
3、元组
"""

app = Flask(__name__)

# 解决中文乱码
app.config['JSON_AS_ASCII'] = False

@app.route("/login/")
def login():
    # 返回[元组]响应response,分三部分(消息主体,状态码,响应头)
    return "<h3>测试返回字符串<h3>"
    # return ("响应体", 200, {"name": "tom", "age": 23})


@app.route("/profile/")
def profile():
    # 返回response[对象]响应
    msg = Response("返回response对象")
    # 返回cookie值
    msg.set_cookie('cookie_name', 'tom')

    return msg


# 自定义设置response响应,如把字典对象转为json对象返回
"""
方法
1、继承Response类
2、实现方法,force_type(cls,rv,environ=None)
3、指定app.response_class为自定义的response对象
"""

class JsonResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """只支持非字符串,非Response对象,非元组时才会调用"""
        if isinstance(response, dict):
            """类型是字典时才会处理"""
            message = jsonify(response)     #转化为json对象
        return super(JsonResponse, cls).force_type(message)
app.response_class(JsonResponse)

@app.route("/resultJson/")
def resultJson():
    return {"name":"jack", "gender":"男", "address":"广东"}


if __name__ == "__main__":
    pass
