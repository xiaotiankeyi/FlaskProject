import graphene
from flask import Flask
from flask_graphql.graphqlview import GraphQLView

"""
创建接口和接口的继承graphene.Interface
garphene.Enum的使用
"""


class Role(graphene.Enum):
    one = 1
    two = 2
    three = 3


class Person(graphene.Interface):
    """定义创建父对象 """
    id = graphene.ID(required=True)
    name = graphene.String(required=True)


class Mouse(graphene.ObjectType):
    # 定义接口,子对象
    class Meta:
        # 继承上面的值,继承多个,规定写死—> interfaces
        interfaces = (Person,)

    # 属于自己的属性
    run = graphene.String(required=True)


class Bird(graphene.ObjectType):
    class Meta:
        interfaces = (Person,)

    # 属于自己的属性
    fly = graphene.String(required=True)


class Result(graphene.ObjectType):
    mouse = graphene.Field(Mouse)
    bird = graphene.Field(Bird)

    person = graphene.Field(Person, type_=graphene.Int(required=True))

    hero = graphene.Field(
        Person,
        required=True,
        type_=graphene.Int(required=True)
    )

    enum = graphene.Field(
        Person,
        required=True,
        type_=Role()
    )

    def resolve_mouse(self, info):
        """id, name继承父类属性,run属于自己的属性"""
        return {'id': 1, 'name': 'jack', 'run': 'jack跑着来的'}

    def resolve_bird(self, info):
        """id, name继承父类属性,fly属于自己的属性"""
        return {'id': 2, 'name': 'Tom', 'fly': 'Tom渣渣叫'}

    def resolve_person(self, info, type_):
        """返回父类,根据参数返回Bird类或是mouse,fly是Bird的属性"""
        """"{person {
                      id
                      name
                      __typename
                      ... on Bird{
                        fly
                      }
                    }}
        """
        """{person(type_:1) {
                      id
                      name
                      ... on Mouse{
                        run
                      }
                    }}
        """
        if type_ == 1:
            return Mouse(id=4, name='jack', run='jack跑着来的')
        return Bird(id=3, name='Tom', fly='Tom渣渣叫')

    def resolve_hero(self, info, type_):
        # 根据type_返回子对象,同时继承了父对象的id,name
        if type_ == 5:
            return Mouse(id=100, name='老鼠', run='跑的很快')
        else:
            return Bird(id=200, name='老鹰', fly='飞的很高')

    def resolve_enum(self, info, type_):
        # 枚举的使用
        if type_ == Role.one:
            return Mouse(id=100, name='老鼠', run='跑的很快')
        elif type_ == Role.two:
            return Bird(id=200, name='老鹰', fly='飞的很高')
        else:
            pass


if __name__ == "__main__":
    schema = graphene.Schema(query=Result)

    app = Flask(__name__)
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    app.run(debug=True)
