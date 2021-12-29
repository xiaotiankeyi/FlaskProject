import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Graphene_demo.graphQL_find.sql_data import human_data, droid_data


def get_character(id):
    # 通过id查询英雄或是机器人,返回"类实例对象"
    print("用户ID", id)
    return human_data.get(id) or droid_data.get(id)


def get_friends(character):
    # 返回human,droid函数
    print("22",character)
    return map(get_character, character.friends)


def get_hero(episode):
    if episode == 5:
        return human_data["1000"]
    return droid_data["2001"]


def get_human(id):
    print('用户22', id)
    return human_data.get(id)


def get_droid(id):
    return droid_data.get(id)
