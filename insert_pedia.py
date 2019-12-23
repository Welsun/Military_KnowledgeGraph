import json
from mongodb_models import Mongo
with open("dataset/hudong_pedia.json","r") as f:
    data = json.load(f)
    client = Mongo().connectDB()
    col = client["pedia_data"]
    for weapon in data:
        att_dict = {}
        key_lists = []
        value_lists = []
        for key, value in weapon.items():

            if key == "baseInfoKeyList":
                key_lists = value.split("##")
            elif key == "baseInfoValueList":
                value_lists = value.split("##")
            else:
                att_dict[key]=value
        if len(key_lists)>0:
            for i in range(len(key_lists)):
                try:
                    att_dict[key_lists[i]] = value_lists[i]
                except:
                    continue
            att_dict["名称"]=att_dict.pop("title")
            att_dict["简介"]=att_dict.pop("detail")
        print(att_dict)
        find = col.find(att_dict)
        if not find:
            col.insert_one(att_dict)
