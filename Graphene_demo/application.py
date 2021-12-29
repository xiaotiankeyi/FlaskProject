from graphene import ObjectType
from graphene import Schema
from graphene import String


class Query(ObjectType):
    """定义规则,规范"""
    hello = String(name='hello',desc=String(default_value='jack'),gender=String(required=True))

    def resolve_hello(self, info, desc, gender):
        """返回结果"""
        return f"hello GraphQL,{desc}, {gender}"


schema = Schema(query=Query)

if __name__ == "__main__":
    """定义查询操作"""
    find_string = """
        {
            hello
        }
        """

    result = schema.execute(find_string)
    print(result.data)
