import pymongo
import json
import jieba
class Mongo():
    client = None
    def __init__(self):
        print("Create a mongodb client class...")

    def connectDB(self):
        client = pymongo.MongoClient(host="10.6.213.55",port=27017)
        return client["military"]

    def insertDB(self,name,data):
        col = self.client[name]
        col.insert(data)



# db = Mongo().connectDB()
# col1= db["weapon_data"]
# col2=db["weapon_datas"]
# for x in col1.find():
#     for key, value in x.items():
#         if key == "产国":
#             x["国家"] = x.pop(key)
#         if key == "大类":
#             x["武器大类"] = x.pop(key)
#         if key == "类型":
#             x["武器类型"] = x.pop(key)
#     col2.insert(x)

# db = Mongo().connectDB()##军事电影
# col = db["pedia_data"]
# count = 0
# for item in (col.find()):
#     try:
#         #if ("《" in item["名称"]) and (("电影" in item["openTypeList"]) or ("影视" in item["openTypeList"]) or ("电视剧" in item["openTypeList"]) ):
#         if "武器" in item["openTypeList"]:
#             count+=1
#             print(item)
#             # col_temp=db["movie"]
#             # col_temp.insert(item)
#     except:
#         continue
# print(count)

# db = Mongo().connectDB()##军事电影
# col = db["pedia_data"]
# count = 0
# for item in (col.find()):
#     try:
#         #if ("《" in item["名称"]) and (("电影" in item["openTypeList"]) or ("影视" in item["openTypeList"]) or ("电视剧" in item["openTypeList"]) ):
#         if "军队"  in item["openTypeList"] and "《" not in item["名称"]:
#             count+=1
#             print(item)
#             # col_temp=db["movie"]
#             # col_temp.insert(item)
#     except:
#         continue
# print(count)

# db = Mongo().connectDB()##军事电影
# col = db["pedia_data"]
# count = 0
# for item in (col.find()):
#     try:
#         #if ("《" in item["名称"]) and (("电影" in item["openTypeList"]) or ("影视" in item["openTypeList"]) or ("电视剧" in item["openTypeList"]) ):
#         if "人物"  in item["openTypeList"] and "《" not in item["名称"]:
#             count+=1
#             print(item)
#             # col_temp=db["movie"]
#             # col_temp.insert(item)
#     except:
#         continue
# print(count)
