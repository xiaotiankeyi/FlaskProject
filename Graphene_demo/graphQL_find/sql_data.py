import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Graphene_demo.graphQL_find.sql_api import Human, Droid

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
