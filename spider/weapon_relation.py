import pymongo
from army_tree_crawler import neo_models
from py2neo import Graph,Node,Relationship,NodeMatcher
from WeaponItems import plane,ship
# neo =neo_models.Neo4j()
# neo.connectDB()
name ="name"
n = Node("总类")
n[name]="军事"
print(n)
# conn = pymongo.MongoClient(host="10.6.213.55",port=27017)
# db =conn['military']['knowledge_base']
# big_classes = ["舰船舰艇","枪械与单兵","坦克装甲车辆","火炮","导弹武器","太空装备","爆炸物"]
#
# big_node = Node("武器第一类",name = big_classes[6])
# neo.graph.create(big_node)
# data = {"大类":big_classes[6]}
# results = db.find(data)
# for result in results:
#     matcher = NodeMatcher(neo.graph)
#     main_node = matcher.match("武器第二类", name=result.get("类型")).first()
#     relation = Relationship(main_node,"belongs_to",big_node)
#     flag = matcher.match(start_node=main_node,end_node = big_node)
#     if not flag:
#         neo.graph.create(relation)