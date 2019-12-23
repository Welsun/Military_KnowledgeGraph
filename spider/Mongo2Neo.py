import pymongo
from army_tree_crawler import neo_models
from py2neo import Graph,Node,Relationship,NodeMatcher
from WeaponItems import plane
neo =neo_models.Neo4j()
neo.connectDB()
#neo.graph.delete_all()
# matcher = NodeMatcher(neo.graph)
# answer = matcher.match("Person",name="Keanu Reeves").first()
labels=["战斗机","攻击机","轰炸机","教练机","预警机","侦察机","反潜机","电子战机","无人机","运输机","飞艇","试验机","加油机","通用飞机","干线","支线","运输直升机","武装直升机","多用途直升机"]
big_class_node = Node("武器第一类",name ="飞行器")
#neo.graph.create(big_class_node)
# for label in labels:
#     main_node = Node("武器第二类",name = label)
#     neo.graph.create(main_node)
#     conn = pymongo.MongoClient(host="10.6.213.55",port=27017)
#     db =conn['military']['knowledge_base']
#
#     data={"类型":label}
#     results =db.find(data)
#     for result in results:
#         p = plane(result)
#         node = Node(label,
#                     name=p.name,
#         country = p.country,
#         # simple_info = p.simple_info,
#         # structure = p.structure,
#         # use_info = p.use_info,
#         # evolution = p.evolution,
#         time_fly = p.time_fly,
#         RDgroup = p.RDgroup,
#         air_layout = p.air_layout,
#         engine_num = p.engine_num,
#         speed = p.speed,
#         passenger = p.passenger,
#         length = p.length,
#         width = p.width,
#         height = p.height,
#         engine = p.engine,
#         max_speed = p.max_speed,
#         max_distance = p.max_distance,
#         first_class = p.first_class,
#         second_class = p.second_class
#         )
#         neo.graph.create(node)
#         relation = Relationship(node,"belongs_to",main_node)
#         neo.graph.create(relation)
matcher = NodeMatcher(neo.graph)
answer = matcher.match("武器第一类",name="飞行器").first()
print(answer)
# for label in labels:
#     answer = matcher.match("武器第二类",name=label).first()
#     relation = Relationship(answer,"belongs_to",big_class_node)
#     neo.graph.create(relation)
