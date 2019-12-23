from neo_models import Neo4j
from py2neo import Graph,Node,Relationship,NodeMatcher
import json
from mongodb_models import Mongo

client = Mongo().connectDB()
col = client["questions_data"]
neo=Neo4j()
neo.connectDB()
index=1
for question in col.find():
    print(question)
    node = Node("军事问题",name="问题"+str(index))
    neo.graph.create(node)
    for key , value in question.items():
        if key=="question":
            node_relation = Node("问题",name=value)
            relation = Relationship(node,"问题是",node_relation)
            neo.graph.create(node_relation)
            neo.graph.create(relation)
        if key=="answer":
            node_relation = Node("答案",name="".join(value))
            relation = Relationship(node,"答案是",node_relation)
            neo.graph.create(node_relation)
            neo.graph.create(relation)

