import json
import ijson
import pymongo
from mongodb_models import Mongo
client=Mongo().connectDB()
col = client["questions_data"]
# with open("dataset/zhidao_qa.json","r") as f:
#     i=0
#     while True:
#         lines = f.readline()
#         if not lines:
#             break
#         que = json.loads(lines)
#         if "军事" in que["tags"]:
#             i+=1
#             que.pop("_id")
#             print(que)
#             jsondata = json.dumps(que,ensure_ascii=False)
#             with open("dataset/military_questions2.json","a") as p:
#                 p.write(jsondata)

with open("dataset/military_questions.json","r+") as p:
    p.seek(0,0)
    p.write("{")




