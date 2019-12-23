import mongodb_models
import neo_models
from mongodb_models import Mongo
from neo_models import Neo4j
from py2neo import Graph,Node,Relationship,NodeMatcher

db = mongodb_models.Mongo().connectDB()
col = db["weapon_datas"]
neo = Neo4j()
neo.connectDB()
#neo.graph.delete_all()
matcher = NodeMatcher(neo.graph)
# for weapon in col.find():
#     weapon.pop("_id")##去除掉id项目，这个插入进入neo4j会导致出错
#     print(weapon)
#     node = Node("武器", name=weapon["名称"])
#     relation_list=[]
#     for key, val in weapon.items():
#         node[key]=val
#     print(node)
#     neo.graph.create(node)
#     print("主节点建造完成")
#     for key, val in weapon.items():
#         node_relation=matcher.match("".join(key),name=val).first()
#         if not node_relation:
#             node_relation=Node("".join(key),name=val)
#         neo.graph.create(node_relation)
#         relation = Relationship(node,"".join(key),node_relation)
#         neo.graph.create(relation)


def insert_pedia(db,neo,matcher):
    col = db["pedia_data"]
    for item in col.find():
        item.pop("_id")
        #if ("战役"in item["openTypeList"]): #and ("装备" in item["openTypeList"]):
        if "人物" in item["openTypeList"] and "《" not in item["名称"]:
            node = matcher.match(name = item["名称"])
            if not node:
                node = Node("人物",name = item["名称"])
                for key,value in item.items():
                    if not key:
                        continue
                    node[key]=value
                neo.graph.create(node)
                print(node)
                print("主节点建造完成")
                for key, val in item.items():
                    if not key:
                        continue
                    node_relation = matcher.match("".join(key), name=val).first()
                    if not node_relation:
                        node_relation = Node("".join(key), name=val)
                    neo.graph.create(node_relation)
                    relation = Relationship(node, "".join(key), node_relation)
                    neo.graph.create(relation)
            else:
                continue


insert_pedia(db,neo,matcher)









    # #判断该国家节点在不在
    # country = weapon["国家"]
    # matcher = NodeMatcher(neo.graph)
    # country_node = matcher.match("国家",name = country).first()
    # if not country_node:
    #     country_node = Node("国家",name = country)
    #     neo.graph.create(country_node)
    # weapon_main_class = weapon["武器大类"]
    # #判断该武器所属的大类节点在不在
    # main_class_node = matcher.match("武器大类",name = weapon_main_class)
    # if not main_class_node:
    #     main_class_node = Node("武器大类",name=weapon_main_class)
    #     neo.graph.create(main_class_node)
    # #判断该武器所属的类型的节点在不在
    # weapon_class = weapon["武器类型"]
    # weapon_class_node = matcher.match("武器类型",name = weapon_class)
    # if not weapon_class_node:
    #     weapon_class_node = Node("武器类型",name = weapon_class)
    #     neo.graph.create(weapon_class_node)
    # #创造武器节点
    # node = Node(weapon_class,name = weapon["名称"])
    # for key,value in weapon.items():
    #     if key !="_id":
    #         node[key]=value
    # neo.graph.create(node)
    # relation1 = Relationship(node,"country is",country_node)
    # relation2 = Relationship(node,"belongs to",weapon_class_node)
    # relation3 = Relationship(weapon_class_node,"belongs to",main_class_node)
    #
    # neo.graph.create(relation1)
    # break