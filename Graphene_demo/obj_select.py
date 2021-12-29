human_data = {}
droid_data = {}

'''
graphQL查询===================== data =========================
'''


def setup():
    global human_data, droid_data
    luke = Human(
        id="1000",
        name="Luke Skywalker",
        friends=["1002", "1003", "2000", "2001"],
        appears_in=[4, 5, 6],
        home_planet="Tatooine",
    )

    vader = Human(
        id="1001",
        name="Darth Vader",
        friends=["1004"],
        appears_in=[4, 5, 6],
        home_planet="Tatooine",
    )

    han = Human(
        id="1002",
        name="Han Solo",
        friends=["1000", "1003", "2001"],
        appears_in=[4, 5, 6],
        home_planet=None,
    )

    leia = Human(
        id="1003",
        name="Leia Organa",
        friends=["1000", "1002", "2000", "2001"],
        appears_in=[4, 5, 6],
        home_planet="Alderaan",
    )

    tarkin = Human(
        id="1004",
        name="Wilhuff Tarkin",
        friends=["1001"],
        appears_in=[4],
        home_planet=None,
    )

    # 英雄数据
    human_data = {
        "1000": luke,
        "1001": vader,
        "1002": han,
        "1003": leia,
        "1004": tarkin,
    }

    c3po = Droid(
        id="2000",
        name="C-3PO",
        friends=["1000", "1002", "1003", "2001"],
        appears_in=[4, 5, 6],
        primary_function="Protocol",
    )

    r2d2 = Droid(
        id="2001",
        name="R2-D2",
        friends=["1000", "1002", "1003"],
        appears_in=[4, 5, 6],
        primary_function="Astromech",
    )

    # 机器人数据
    droid_data = {"2000": c3po, "2001": r2d2}


def get_character(id):
    # 通过id查询英雄或是机器人,返回"类实例对象"
    return human_data.get(id) or droid_data.get(id)


def get_friends(character):
    return map(get_character, character.friends)


def get_hero(episode):
    if episode == 5:
        return human_data["1000"]
    return droid_data["2001"]


def get_human(id):
    return human_data.get(id)


def get_droid(id):
    return droid_data.get(id)


'''
===================== schema =========================
'''

import graphene
from flask import Flask
from flask_graphql import GraphQLView


class Episode(graphene.Enum):  # 剧集
    NEWHOPE = 4  # 星球大战4 新希望
    EMPIRE = 5  # 黑金帝国
    JEDI = 6  # 星球大战 绝地


class Character(graphene.Interface):  # 角色
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
    setup()

    schema = graphene.Schema(query=Query)

    app = Flask(__name__)
    app.add_url_rule('/graphql',
                     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(debug=True)
