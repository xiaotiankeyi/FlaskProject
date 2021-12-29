"""
定义枚举,父类接口,子类接口,查询接口
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import graphene


class Episode(graphene.Enum):  # 剧集
    """
    枚举
    """
    NEWHOPE = 4  # 星球大战4 新希望
    EMPIRE = 5  # 黑金帝国
    JEDI = 6  # 星球大战 绝地


class Character(graphene.Interface):  # 角色
    """
    角色,父类公共属性
    """
    id = graphene.ID()
    name = graphene.String()
    friends = graphene.List(lambda: Character)
    appears_in = graphene.List(Episode)  # 出演

    def resolve_friends(self, info):
        # The character friends is a list of strings
        return [get_character(f) for f in self.friends]


class Human(graphene.ObjectType):  # 人类
    class Meta:
        interfaces = (Character,)

    home_planet = graphene.String()  # 地球家园


class Droid(graphene.ObjectType):  # 机器人
    class Meta:
        interfaces = (Character,)

    primary_function = graphene.String()  # 主要功能


class Query(graphene.ObjectType):
    hero = graphene.Field(Character, episode=Episode())
    human = graphene.Field(Human, id=graphene.String())
    droid = graphene.Field(Droid, id=graphene.String())

    def resolve_hero(root, info, episode=None):
        return get_hero(episode)

    def resolve_human(root, info, id):
        return get_human(id)

    def resolve_droid(root, info, id):
        return get_droid(id)


if __name__ == '__main__':
    from Graphene_demo.graphQL_find.sql_data import setup
    setup()

    from flask import Flask
    from flask_graphql import GraphQLView
    from Graphene_demo.graphQL_find.sql_find_way import get_character, \
        get_droid, get_human, get_hero

    schema = graphene.Schema(query=Query)
    app = Flask(__name__)
    app.add_url_rule('/graphql',
                     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(debug=True)
